from function import *

input="D:/MIR/Data1"
output0="D:/MIR/DeepLearning"
output1="D:/MIR/DeepLearning_1"

modeldensenet121 = applications.densenet.DenseNet121(weights='imagenet')
generate(input,output0,"DenseNet121",modeldensenet121,applications.densenet.preprocess_input)
modeldensenet121_1 = Model(inputs=modeldensenet121.input, outputs=modeldensenet121.layers[-2].output)
generate(input,output1,"DenseNet121_1",modeldensenet121_1,applications.densenet.preprocess_input)

modeldensenet169 = applications.densenet.DenseNet169(weights='imagenet')
generate(input,output0,"DenseNet169",modeldensenet169,applications.densenet.preprocess_input)
modeldensenet169_1 = Model(inputs=modeldensenet169.input, outputs=modeldensenet169.layers[-2].output)
generate(input,output1,"DenseNet169_1",modeldensenet169_1,applications.densenet.preprocess_input)

modeldensenet201 = applications.densenet.DenseNet201(weights='imagenet')
generate(input,output0,"DenseNet201",modeldensenet201,applications.densenet.preprocess_input)
modeldensenet201_1 = Model(inputs=modeldensenet201.input, outputs=modeldensenet201.layers[-2].output)
generate(input,output1,"DenseNet201_1",modeldensenet201_1,applications.densenet.preprocess_input)