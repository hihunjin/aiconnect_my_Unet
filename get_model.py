import torch
from model import Model

dummy_input = torch.rand((2,3,512,512))
Model(dummy_input)
print('loading model finished')