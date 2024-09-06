import torch
from api import app
from api.model import LSTM
import json
import numpy as np
def Build_Model():
    input_size = app.config["INPUT_SIZE"]
    hidden_size = app.config["HIDDEN_SIZE"]
    output_size = app.config["OUTPUT_SIZE"]
    seq_l = app.config["SEQ_LENGTH"]
    model_path = app.config["MODEL_PATH"]

    net = LSTM(input_size, hidden_size, output_size, seq_l)  # 网络
    net.load_state_dict(torch.load(model_path))
    return net

def Build_Mapping():
    component_type_mapping = app.config["COMPONENT_TYPE_MAPPING"]
    with open(component_type_mapping, 'r') as file:
        data = json.load(file)
    return data

def Find_Next_Component(Components, net, data):

    components_list = []
    for key in Components:
        components_list.append(data[key])

    int_arrays = [[int(digit) for digit in string] for string in components_list]
    x_tensor = torch.tensor(int_arrays, dtype=torch.float)
    x_tensor = x_tensor.unsqueeze(0)
    y_tensor = net(x_tensor)
    y_tensor = y_tensor.detach().numpy()

    dict_values_int_array = {key: [int(char) for char in value] for key, value in data.items()}
    cc = Similarity_search(dict_values_int_array, y_tensor)
    return cc

def Similarity_search(d, value):
    max_similarity = 0
    cc = None
    for key, val in d.items():
        dot_product = np.dot(val, value[0])

        # 计算每个数组的欧几里得范数
        norm_array1 = np.linalg.norm(val)
        norm_array2 = np.linalg.norm(value)
        # 计算余弦相似度
        cosine_similarity = dot_product / (norm_array1 * norm_array2)

        if cosine_similarity > max_similarity:
            cc = key
            max_similarity = cosine_similarity
    return cc

def Inference_Component(Components: list[str]) -> str:
    while len(Components) != 6:
        Components.insert(0, "null")
    net = Build_Model()
    data = Build_Mapping()
    Next_Component = Find_Next_Component(Components, net, data)
    return Next_Component