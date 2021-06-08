# Install
```sh
pip install requirement.txt
```

# Create docker container

```sh
nvidia-docker run -it -v $(pwd):/workspace pytorch/pytorch:1.7.0-cuda11.0-cudnn8-runtime /bin/bash
```

# Demo

```python
import torch
from model import Model

dummy_input = torch.rand((2,3,512,512))
Model(dummy_input)
```
