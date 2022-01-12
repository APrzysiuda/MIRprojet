from function import *

input="D:/MIR/Data"
output="D:/MIR/Test"

modeldensenet121 = applications.densenet.DenseNet121(weights='imagenet',pooling="max")
generate(input,output,"DenseNet121",modeldensenet121,applications.densenet.preprocess_input)
modeldensenet121_1 = Model(inputs=modeldensenet121.input, outputs=modeldensenet121.layers[-2].output)
generate(input,output,"DenseNet121_1",modeldensenet121_1,applications.densenet.preprocess_input)

modeldensenet121_10 = applications.densenet.DenseNet121(weights='imagenet',pooling="avg")
generate(input,output,"DenseNet121_10",modeldensenet121_10,applications.densenet.preprocess_input)
modeldensenet121_1_10 = Model(inputs=modeldensenet121_10.input, outputs=modeldensenet121_10.layers[-2].output)
generate(input,output,"DenseNet121_1_10",modeldensenet121_1_10,applications.densenet.preprocess_input)