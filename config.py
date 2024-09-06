class Config:
    HOST = "0.0.0.0"
    PORT = "8050"

    # LSTM_model
    INPUT_SIZE = 10
    HIDDEN_SIZE = 256
    OUTPUT_SIZE = 10
    SEQ_LENGTH = 6
    MODEL_PATH = r"./DL_model/LSTM/demo_model.pth"

    # Component
    COMPONENT_TYPE_MAPPING = r"./data/definition.json"

    # record
    FIELDNAMES = [
        'Components',
        'Predicted_Components',
        'User_Feedback',
        'User_Select_Components',
        'CreationTime'
    ]
    FILENAME = r'./data/FeedbackRecord/data.csv'