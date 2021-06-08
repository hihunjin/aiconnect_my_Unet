import os

def Get_weight():
    print('Please wait : 0/3')
    os.system('pip install gdown  > /dev/null')
    print('Please wait : 1/3')
    if not os.path.isfile('model_best.pth.tar'):
        os.system('gdown https://drive.google.com/uc?id=1Ysh-QhyvZ4q2Q8_zjlDo0uituARrQjWZ > /dev/null')
    # os.system('apt update -y')
    # os.system('apt install git -y')
    print('Please wait : 2/3')
    os.system('pip install segmentation-models-pytorch > /dev/null')
    print('Please wait : 3/3')
