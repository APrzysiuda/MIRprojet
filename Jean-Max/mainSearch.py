from search import *

parameters=[]

dataPath="D:\MIR\Old\Data"
featurePath = "D:\MIR\Old\Indicateur"
imageName="1_2_Kia_sorento_1759.jpg"

parameters.append(Parameter("HSV","Euclidienne",1))
#parameters.append(Parameter("BGR","Chicarre",0))

image=cv2.imread(os.path.join(dataPath,imageName))

ordering,chrono=search(dataPath,featurePath,image,parameters)

print(str(chrono/60),"minutes")
for ele in ordering[:100]:
    print(ele.score,ele.imageName,os.path.join(dataPath,ele.imageName+".jpg"))

