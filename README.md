# Install
```sh
pip install requirement.txt
```

# Create docker container

```sh
nvidia-docker run -it --shm-size=8gb --cpus=8 -e NVIDIA_VISIBLE_DEVICES=0,1 -v $(pwd):/workspace pytorch/pytorch:1.7.0-cuda11.0-cudnn8-runtime /bin/bash
```

# Demo

```python
import torch
from model import Model

dummy_input = torch.rand((2,3,512,512))
Model(dummy_input)
```
