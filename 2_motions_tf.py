import os
import io
import sys
import glob
import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import imshow
import scipy
from PIL import Image
import tensorflow as tf
import random
from tensorflow.keras import layers
import time
from tensorflow.keras import datasets, layers, models, applications

os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

#directions = ['five', 'one']
def load_images(globpath):
    for i, image in enumerate(globpath):
        with open(image, 'rb') as file:
            img = Image.open(file)
            img = img.resize((224, 224))
            np_img = np.array(img)
            my_list.append(np_img)

my_list = []
load_images(glob.glob("dataset3/five*.JPG"))
load_images(glob.glob("dataset3/one*.JPG"))
my_list = np.array(my_list)
print('my_list.shape: ', my_list.shape)

# 0 five (140), one (140)
labels_ = [0,0,0,0,0,0,0,0,0,0, #1
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,#5
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,#10
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        1,1,1,1,1,1,1,1,1,1,#1
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,#5
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,#10
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1
        ]
print("num labels: ",len(labels_))
labels_ = np.array(labels_)


p = np.random.permutation(len(my_list))
X_orig = my_list[p]
Y_orig = labels_[p]

X_test_orig = X_orig[0:50]
Y_test_orig = Y_orig[0:50]
X_dev_orig = X_orig[51:101]
Y_dev_orig = Y_orig[51:101]
X_train_orig = X_orig[102:len(labels_)]
Y_train_orig = Y_orig[102:len(labels_)]

X_train = X_train_orig/255
X_dev = X_dev_orig/255
X_test = X_test_orig/255

def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y

Y_train = convert_to_one_hot(Y_train_orig, 2).T
Y_test = convert_to_one_hot(Y_test_orig, 2).T
Y_dev = convert_to_one_hot(Y_dev_orig, 2).T

#define model
print('up to here')

model = tf.keras.Sequential()
model.add(layers.Conv2D(8, (11, 11), activation='relu', input_shape=(224, 224, 3), data_format='channels_last'))
model.add(layers.MaxPooling2D((2, 2), (2, 2), data_format='channels_last'))

model.add(layers.Conv2D(16, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.Conv2D(16, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.MaxPooling2D((2, 2), (2, 2), data_format='channels_last'))

model.add(layers.Conv2D(32, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.Conv2D(32, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.Conv2D(32, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.MaxPooling2D((2, 2), (2, 2), data_format='channels_last'))

model.add(layers.Conv2D(64, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.Conv2D(64, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.Conv2D(64, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.MaxPooling2D((2, 2), (2, 2), data_format='channels_last'))

model.add(layers.Conv2D(128, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.Conv2D(128, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.Conv2D(128, (3, 3), activation='relu', data_format='channels_last'))
model.add(layers.MaxPooling2D((2, 2), (2, 2), data_format='channels_last'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu', input_dim=128*3*3))
model.add(layers.Dropout(rate=0.5))

model.add(layers.Dense(64, activation='relu', input_dim=32))
model.add(layers.Dropout(rate=0.5))

model.add(layers.Dense(2, activation='sigmoid', input_dim=8))

#print summary
model.summary()

#compile tf.keras.optimizers.Adam() tf.keras.losses.BinaryCrossentropy()
model.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['accuracy'])

#train :)
print('==========Training==========')
training = model.fit(X_train, Y_train, epochs=15, steps_per_epoch=10)
plt.plot(training.history['acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

#dev
print('==========Validating==========')
dev_loss, dev_acc = model.evaluate(X_dev, Y_dev)
print('validating: ', dev_loss, ' ', dev_acc)


#test
print('==========Testing==========')
test_loss, test_acc = model.evaluate(X_test, Y_test)
print('testing: ', test_loss, ' ', test_acc)

model.save('the_h5_model.h5')
print('the end, saved')


