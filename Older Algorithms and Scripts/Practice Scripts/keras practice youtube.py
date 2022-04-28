import csv
import numpy as np
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy

a_dict = {}
b_dict = {}

a_datax = []
a_datay = []
b_datax = []
b_datay = []

a_trainx = []
a_trainy = []

b_testx = []
b_testy = []

# Converts the csv to a dict
# with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\charlotte_data.csv","r") as file1:
with open(r"C:\Users\Pecha Berry\Desktop\ASU-CapWeather\WeatherAPIs\API Outputs\historic_charlotte_data.csv","r") as file1:
    dict_reader = csv.DictReader(file1)

    for row in dict_reader:
        for column, value in row.items():
            a_dict.setdefault(column, []).append(value)

# Converts the csv to a dict
# with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\charlotte_data.csv","r") as file1:
with open(r"C:\Users\Pecha Berry\Desktop\ASU-CapWeather\WeatherAPIs\API Outputs\charlotte_data.csv","r") as file1:
    dict_reader = csv.DictReader(file1)

    for row in dict_reader:
        for column, value in row.items():
            b_dict.setdefault(column, []).append(value)

# Gets the temperature to a list to be processed.
a_datay = a_dict['Temperature']

# Lables for the x axis.
a_count = 0
a_datax = []
for i in range (len(a_dict['Date'])):
    a_count +=1
    a_datax.append(a_count)

a_trainx = np.array(a_datax)
a_trainy = np.array(a_datay)

print (a_trainx)
print (a_trainy)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_a_trainx = scaler.fit_transform(a_trainx.reshape(-1,1))
scaled_a_trainy = scaler.fit_transform(a_trainy.reshape(-1,1))