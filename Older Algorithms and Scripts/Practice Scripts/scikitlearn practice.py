#!/bin/bash

import matplotlib
import pandas as pd
import numpy as np
import matplotlib as mp

from sklearn import datasets, linear_model
from sklearn.impute import SimpleImputer
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate


df = pd.read_csv(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\atlanta_data_02.csv")
#df = pd.read_csv(r"C:\Users\Pecha Berry\Desktop\ASU-CapWeather\WeatherAPIs\API Outputs\atlanta_data_02.csv")
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)

features_df = pd.get_dummies(df, columns=['date','pressure','pattern','wind_speed','wind_degree'])

X = np.array(features_df)
y = np.array(df['temperature'])

model = ensemble.GradientBoostingRegressor(
    n_estimators=250,
    learning_rate=0.1,
    max_depth=5,
    min_samples_split=4,
    min_samples_leaf=6,
    max_features=0.6,
    loss='huber'
)

# Split data into test/train set (70/30 split) and shuffle
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Run model on training data
model.fit(X_train, y_train)

# Setting X values for predictions to the y
# #
x_train_tofile = model.predict(X_train)
x_test_tofile = model.predict(X_test)

# Check model accuracy (up to two decimal places)
a_mse = mean_absolute_error(y_train, model.predict(X_train))
a_accuracy = 100-a_mse
b_mse = mean_absolute_error(y_test, model.predict(X_test))
b_accuracy = 100-b_mse
print ("Training Set Mean Absolute Error Rate: %.2f" % a_mse)
print ("Training Set Mean Absolute Accuracy Rate: %.2f" % a_accuracy )
print ("Test Set Mean Absolute Error Rare: %.2f" % b_mse)
print ("Test Set Mean Absolute Accuracy Rate: %.2f" % b_accuracy )

# Validation set
lasso = linear_model.Lasso()
df_pred = cross_val_predict(lasso, X, y, cv=3)
df_results = cross_validate(lasso, X, y, cv=3)
print ( "Validation Score: %.4f" % df_results['test_score'][0] )
print ( "Validation Predictions: \n"+str(df_pred) )

imputer = SimpleImputer()
mdl = ensemble.RandomForestRegressor(
    n_estimators=100,
    random_state=0,
    n_jobs=6
)

mdl.fit(X_train, y_train)
imputer.fit_transform(X_train)
xval = imputer.transform(X_train)

p = mdl.predict(xval)
mdl_mape = mean_absolute_error(y_train, p)
print ( str(p[0])+","+str(y_train[0]) )
