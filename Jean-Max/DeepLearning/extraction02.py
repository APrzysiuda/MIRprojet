from function import *

input="D:/MIR/Data1"
output0="D:/MIR/DeepLearning"
output1="D:/MIR/DeepLearning_1"

modelvgg16 = applications.vgg16.VGG16(weights='imagenet')
generate(input,output0,"VGG16",modelvgg16,applications.vgg16.preprocess_input)
modelvgg16_1 = Model(inputs=modelvgg16.input, outputs=modelvgg16.layers[-2].output)
generate(input,output1,"VGG16_1",modelvgg16_1,applications.vgg16.preprocess_input)

modelvgg19 = applications.vgg19.VGG19(weights='imagenet')
generate(input,output0,"VGG19",modelvgg19,applications.vgg19.preprocess_input)
modelvgg19_1 = Model(inputs=modelvgg19.input, outputs=modelvgg19.layers[-2].output)
generate(input,output1,"VGG19_1",modelvgg19_1,applications.vgg19.preprocess_input)

modelresnet50 = applications.resnet50.ResNet50(weights='imagenet')
generate(input,output0,"ResNet50",modelresnet50,applications.resnet50.preprocess_input)
modelresnet50_1 = Model(inputs=modelresnet50.input, outputs=modelresnet50.layers[-2].output)
generate(input,output1,"ResNet50_1",modelresnet50_1,applications.resnet50.preprocess_input)