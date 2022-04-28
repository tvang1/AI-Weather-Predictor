# Example Import for Keras API.
# 
# tensorflow module has to be installed to the OS or through
# python 3.6 or greater.
# 
# pip3 install tensorflow
# 
# Afterwards, follow this import for the .py file for implmentation.
# 
# #

import numpy as np
from random import randint
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy

train_label = []
train_sample = []

test_label = []
test_sample = []

for i in range(50):
    random_young = randint(13,64)
    train_sample.append(random_young)
    train_label.append(1)

    random_old = randint(65,100)
    train_sample.append(random_old)
    train_label.append(0)

for i in range(1000):
    random_young = randint(13,64)
    train_sample.append(random_young)
    train_label.append(0)

    random_old = randint(65,100)
    train_sample.append(random_old)
    train_label.append(1)

train_label = np.array(train_label)
train_sample = np.array(train_sample)
train_label, train_sample = shuffle(train_label, train_sample)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_sample = scaler.fit_transform(train_sample.reshape(-1,1))

model = Sequential([
    Dense(units=16, input_shape=(1,), activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=2, activation='softmax')
])

#model.summary()

model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x=scaled_train_sample, y=train_label, validation_split=0.1, batch_size=10, epochs=30, shuffle=True, verbose=2)