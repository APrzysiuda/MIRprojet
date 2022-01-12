import numpy as np

from function1 import *

input="D:/MIR/Data"
output="D:/MIR/Indicateur"

for indicateurName in os.listdir(output):
    path = os.path.join(output, indicateurName)
    listFile=os.listdir(path)
    path1 = os.path.join(path, listFile[0])
    vector = np.loadtxt(path1)
    print(indicateurName,np.shape(vector))