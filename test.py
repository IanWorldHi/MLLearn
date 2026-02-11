#Note: Do not need to spend an exessive amountof time here

import torch
from torch.utils.data import Dataset
from torchvision import datasets   
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import numpy as np
#Need to learn some numpy I guess
# Faster becuase all in same part of memory, regular python lists are not

#Can run on GPU, which is faster for large computations, but not all operations are supported on GPU, so need to check documentation
#Compared to CPU so like in google collab you can specify it with settings

#These two are for Loading Dataset
training_data = datasets.FashionMNIST(
    root="data", #path where data stoerd
    train=True, 
    download=True, #downloads from internet if not in root
    transform=ToTensor() 
)
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)


#Tensors: like arrays/matrices to encode inputs/outputs
#Tensor Operations: https://docs.pytorch.org/docs/stable/torch.html
#Can auto infer type
data = [[1, 2], [1, 3]]
torchdata = torch.tensor(data)  
nparr = np.array(data)
torcharr = torch.from_numpy(nparr)
torcharr.shape
torcharr.dtype #default float32
torcharr.device
awfhejka = torch.ones((5, 3), dtype=torch.float64, device='cpu')

""" print(nparr)
print(torcharr) """












