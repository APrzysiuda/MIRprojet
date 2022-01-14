from function import *

input="D:/MIR/Data"

model=k.applications.densenet.DenseNet121
modelName="h5/DenseNet121.h5"
setupModel(model,modelName)

model=k.applications.densenet.DenseNet169
modelName="h5/DenseNet169.h5"
setupModel(model,modelName)

model=k.applications.densenet.DenseNet201
modelName="h5/DenseNet201.h5"
setupModel(model,modelName)

model=k.applications.vgg16.VGG16
modelName="h5/VGG16.h5"
setupModel(model,modelName)

model=k.applications.vgg19.VGG19
modelName="h5/VGG19.h5"
setupModel(model,modelName)

model=k.applications.resnet50.ResNet50
modelName="h5/ResNet50.h5"
setupModel(model,modelName)

model=k.applications.mobilenet.MobileNet
modelName="h5/MobileNet.h5"
setupModel(model,modelName)

model=k.applications.xception.Xception
modelName="h5/Xception.h5"
setupModel(model,modelName)

model=k.applications.inception_v3.InceptionV3
modelName="h5/InceptionV3.h5"
setupModel(model,modelName)

model=k.applications.inception_resnet_v2.InceptionResNetV2
modelName="h5/InceptionResNetV2.h5"
setupModel(model,modelName)
