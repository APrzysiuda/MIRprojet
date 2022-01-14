import numpy as np
import os
import shutil
import tensorflow.keras as k


def setupModel(originalModel, modelName):
    width = 224
    height = 224
    trainPath = "D:\MIR\DataSet\Train"
    testPath = "D:\MIR\DataSet\Test"

    datagen = k.preprocessing.image.ImageDataGenerator(rescale=1. / 255)

    trainData = datagen.flow_from_directory(trainPath, shuffle=True, target_size=(width, height))

    testData = datagen.flow_from_directory(testPath, shuffle=False, target_size=(width, height))

    model = originalModel(weights='imagenet', include_top=False, input_shape=(width, height, 3))

    earlyStopping = k.callbacks.EarlyStopping(monitor='loss', patience=3)

    model.compile(
        #optimizer="Adam",#0.001
        #loss = "CategoricalCrossentropy",
        #metrics = ["Accuracy"]
        optimizer=k.optimizers.RMSprop(),
        loss=k.losses.SparseCategoricalCrossentropy(),
        metrics=[k.metrics.SparseCategoricalAccuracy()]
    )

    model.fit(
        trainData,
        batch_size=32,
        epochs=100,
        validation_data=testData,
        callbacks=[earlyStopping]
    )

    model.save_weights(modelName)
