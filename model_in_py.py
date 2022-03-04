
import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt
from sklearn.model_selection import KFold
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D,Dense, Flatten
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import Model

(trainX,trainY),(testX,testY) = mnist.load_data()
trainX = trainX.reshape((trainX.shape[0], 28, 28,1)).astype('float32')
testX = testX.reshape((testX.shape[0], 28, 28,1)).astype('float32')
trainX=trainX/255
testX=testX/255

trainY = to_categorical(trainY,num_classes=10)
testY = to_categorical(testY,num_classes=10)

model= tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3), padding='same', activation='relu',input_shape=(28,28,1)),
  tf.keras.layers.MaxPooling2D(pool_size=(2,2),strides=1,padding='same'),                
  tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3), padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(pool_size=(2,2),strides=1,padding='same'),                   
  tf.keras.layers.Conv2D(filters=1,kernel_size=(3,3), padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(pool_size=(2,2),strides=1,padding='same'),       
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128,activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10,activation='sigmoid')
])
model.compile(optimizer='Adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary()

history=model.fit(trainX,trainY,epochs=50,validation_data=(testX,testY))

result=model.evaluate(testX,testY)
print('Accuracy',result[1]*100)

pdt=model.predict(testX)
print(pdt[11],testY[11])
plt.imshow(testX[11].reshape(28,28))

testX.shape



