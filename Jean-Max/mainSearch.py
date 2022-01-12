from search import *

parameters=[]

dataPath="D:\MIR\Old\Data"
featurePath = "D:\MIR\Old\Indicateur"
imageName="1_2_Kia_sorento_1759.jpg"

parameters.append(Parameter("Euclidienne","HSV",1))
parameters.append(Parameter("Chicarre","BGR",0))

image=cv2.imread(os.path.join(dataPath,imageName))

ordering,time=search(dataPath,featurePath,image,parameters)

for ele in ordering[:100]:
    print(ele.score,ele.imageName)

