import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

def df_to_X_y(df, size):
  df_as_np = df.to_numpy()
  X = []
  y = []
  for i in range(len(df_as_np)-size):
    row = [[a] for a in df_as_np[i:i+size]]
    X.append(row)
    label = df_as_np[i+size]
    y.append(label)
  return np.array(X), np.array(y)

csv_path = (r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\historic_atlanta_5Years.csv")
#csv_path = (r"C:\Users\Pecha Berry\Desktop\ASU-CapWeather\WeatherAPIs\API Outputs\historic_atlanta_5Years.csv")

df = pd.read_csv(csv_path)

#print (df.shape)

size = 3
x1, y1 = df_to_X_y(df['Temperature'], size)

x1, y1 = shuffle(x1, y1)

#print (df_to_X_y(df['Temperature'], size))

x_train, y_train = x1[:1500], y1[:1500]
x_val, y_val = x1[1500:1900], y1[1500:1900]
x_test, y_test = x1[2192:], y1[2192:]

a_model = Sequential()
a_model.add(InputLayer((3,1)))
a_model.add(LSTM(64))
a_model.add(Dense(16, 'relu'))
a_model.add(Dense(2, 'softmax'))
a_model.add(Dense(1, 'linear'))

a_model.summary()

cp1 = ModelCheckpoint('a_model/', save_best_only=True)
a_model.compile(loss='categorical_crossentropy', run_eagerly=True, optimizer=Adam(learning_rate=0.1), metrics=["accuracy"])

a_model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size=10, epochs=30, callbacks=[cp1], verbose=2)

a_model = load_model('a_model/')

train_predictions = a_model.predict(x_train).flatten()
train_results = pd.DataFrame(data={'Train Predictions':train_predictions, 'Train Actuals':y_train})

print ( train_results )