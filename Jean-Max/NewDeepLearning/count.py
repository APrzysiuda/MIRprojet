import numpy as np
import os

input="D:\MIR\Old\Data"

res=np.zeros(10)
for imageName in os.listdir(input):
    for i in range(10):
        if int(imageName.split("_")[0])==i:
            res[i]+=1
            break
print(res)