import torch
import numpy as np
#Need to learn some numpy I guess
# Faster becuase all in same part of memory, regular python lists are not


#Tensors: like arrays/matrices to encode inputs/outputs
#Can auto infer type
data = [[1, 2], [1, 3]]
torchdata = torch.tensor(data)  
nparr = np.array(data)
torcharr = torch.from_numpy(nparr)
torcharr.shape
torcharr.dtype
torcharr.device

print(nparr)
print(torcharr)











