from function import *

input="D:/MIR/Data1"
output0="D:/MIR/DeepLearning"
output1="D:/MIR/DeepLearning_1"

modelmobilenet = applications.mobilenet.MobileNet(weights='imagenet')
generate(input,output0,"MobileNet",modelmobilenet,applications.mobilenet.preprocess_input)
modelmobilenet_1 = Model(inputs=modelmobilenet.input, outputs=modelmobilenet.layers[-2].output)
generate(input,output1,"MobileNet_1",modelmobilenet_1,applications.mobilenet.preprocess_input)

modelxception = applications.xception.Xception(weights='imagenet')
generate(input,output0,"Xception",modelxception,applications.xception.preprocess_input)
modelxception_1 = Model(inputs=modelxception.input, outputs=modelxception.layers[-2].output)
generate(input,output1,"Xception_1",modelxception_1,applications.xception.preprocess_input)

modelinception_v3 = applications.inception_v3.InceptionV3(weights='imagenet')
modelinception_v3_1 = Model(inputs=modelinception_v3.input, outputs=modelinception_v3.layers[-2].output)
generate(input,output1,"InceptionV3_1",modelinception_v3_1,applications.inception_v3.preprocess_input)

modelinception_resnet_v2 = applications.inception_resnet_v2.InceptionResNetV2(weights='imagenet')
generate(input,output0,"InceptionResNetV2",modelinception_resnet_v2,applications.inception_resnet_v2.preprocess_input)
modelinception_resnet_v2_1 = Model(inputs=modelinception_resnet_v2.input, outputs=modelinception_resnet_v2.layers[-2].output)
generate(input,output1,"InceptionResNetV2_1",modelinception_resnet_v2_1,applications.inception_resnet_v2.preprocess_input)