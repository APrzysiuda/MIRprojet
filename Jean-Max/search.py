import time

from distance import *
from extraction import *

class Parameter:
    def __init__(self,distanceName,featureName,wheight):
        self.distanceName=distanceName
        self.featureName=featureName
        self.wheight=wheight

class Image:
    def __init__(self,imageName):
        self.imageName=imageName
        self.score=0
    def addScore(self,score):
        self.score+=score

    def __str__(self):
        return self.imageName + ' - ' + self.requestName + ' - ' + self.distanceName + ' - ' + str(
            self.distance) + ' - ' + str(self.brand)

def search(dataPath,featurePath,requestImage,parameters):
    start=time.time()
    ordering=[]
    for imageName in os.listdir(dataPath):
        imageName=imageName.split(".")[0]
        ordering.append(Image(imageName))
    for parameter in parameters:
        requestFeature = featureExtraction(requestImage,parameter.featureName)
        for image in ordering:
            comparisonFeature=np.loadtxt(os.path.join(featurePath,parameter.featureName,image.imageName+".txt"))
            image.addScore(parameter.wheight*distance(requestFeature,comparisonFeature,parameter.distanceName))
    ordering.sort(key=lambda x: x.score)
    chrono=time.time()-start
    return ordering,time