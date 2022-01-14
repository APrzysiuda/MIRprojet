import os.path

from function import *

input="D:\MIR\Old\Data"
outputTrain="D:\MIR\DataSet\Train"
outputTest="D:\MIR\DataSet\Test"

imageNames=os.listdir(input)
#n=int(len(imageNames)*0.8)
#print(n)
np.random.shuffle(imageNames)

trainImageNames=imageNames[:11328]
testImageNames=imageNames[11328:14144]
#print(len(trainImageNames),len(testImageNames))

for imageName in trainImageNames:
    brand=imageName.split("_")[0]
    shutil.copy(os.path.join(input,imageName), os.path.join(outputTrain,brand))
for imageName in testImageNames:
    brand=imageName.split("_")[0]
    shutil.copy(os.path.join(input,imageName), os.path.join(outputTest,brand))