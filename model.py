import torch.nn as nn 

class VGG(nn.Module):
    def __init__(self):
        super(VGG, nn.Module).__init__()
    

    def forward(self, x):
        return x 