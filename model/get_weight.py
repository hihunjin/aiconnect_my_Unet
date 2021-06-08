import os

def Get_weight():
    os.system('pip install gdown')
    if not os.path.isfile('model_best.pth.tar'):
        os.system('gdown https://drive.google.com/uc?id=1Ysh-QhyvZ4q2Q8_zjlDo0uituARrQjWZ')
    # os.system('apt update -y')
    # os.system('apt install git -y')
    os.system('pip install segmentation-models-pytorch')