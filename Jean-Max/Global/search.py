from distance import *
from extraction import *

class Parameter:
    def __init__(self,featureName,distanceName,wheight):
        self.featureName=featureName
        self.distanceName = distanceName
        self.wheight=wheight

class Image:
    def __init__(self,imageName):
        self.imageName=imageName
        self.score=0
    def addScore(self,score):
        self.score+=score

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
    return ordering,chrono