import torch
import torch.nn as nn

from .get_weight import Get_weight

Get_weight()
import segmentation_models_pytorch as smp
Model = smp.DeepLabV3Plus('resnet50', classes=2, encoder_weights=None)
checkpoint = torch.load('model_best.pth.tar')
Model.load_state_dict(checkpoint['state_dict'])