from torch import nn

class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, seq_l):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.linear = nn.Linear(hidden_size * seq_l, output_size)

    def forward(self, x_in):
        x_in, _ = self.lstm(x_in)
        b, s, f = x_in.shape  # batch_size, sequence_length, feature_number
        x_in = x_in.reshape(b, s * f)
        x_in = self.linear(x_in)

        return x_in