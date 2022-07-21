#!/bin/bash
import pandas as pd
import numpy as np

from sklearn.utils import *
from sklearn import ensemble
from sklearn import linear_model
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

# Choose correct file path for evaluating model.
# #

df = pd.read_csv(r"D:\GitDepositories\Simple-Weather-Predictor\WeatherAPIs\API Outputs\castle_rock_data.csv")
#df = pd.read_csv(r"D:\GitDepositories\Simple-Weather-Predictor\WeatherAPIs\API Outputs\denver_data.csv")
#df = pd.read_csv(r"D:\GitDepositories\Simple-Weather-Predictor\WeatherAPIs\API Outputs\boulder_data.csv")

df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)

# X represents the features that will be compared to the y.
# X values will try to predict according to values in y and 
# X will try produce predictions with values matching y.
# 
# get_dummies will make up the 'X' and other columns. It
# converts columns into evaulables.
#
# Please chgange the 'y' and 'x' interchangably 
# when making different predictions.
# 
# columns=['date','pattern','temperature','pressure','wind_speed','wind_degree']
# #
features_df = pd.get_dummies(df, columns=['date','pattern','wind_degree','pressure','wind_speed'])
X = np.array(features_df)
y = np.array(df['temperature'])

# Split data into test/train set (70/30 split) and shuffle
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# 
# Above is the format from the book. random_state removed in order to get varied results.
# #
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Setting up model. Make sure to look at "ensemble" documentation
# for correct alterations.
# #
model = ensemble.GradientBoostingRegressor(
    n_estimators=250,
    learning_rate=0.1,
    max_depth=5,
    min_samples_split=4,
    min_samples_leaf=6,
    max_features=0.6,
    loss='huber'
)

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
# 
# Make sure this set is not overfitting. If not, then
# the algorithm is successful.
# #
lasso = linear_model.Lasso()
df_vpred = cross_val_predict(lasso, X, y, cv=3)
df_vresults = cross_validate(lasso, X, y, cv=3)
val_accuracy =  df_vresults['test_score'][0]*100
val_error = 100-val_accuracy
print ("Validation Error Rate: %.2f" % val_error)
print ("Validation Accuracy Rate: %.2f" % val_accuracy)

# Prediction Model
# 
# Uses imputer and RandomForestRegressor to make predictions.
# Export these values for prediction for the data.
# #
imputer = SimpleImputer()
p_mdl = ensemble.RandomForestRegressor(
    n_estimators=100,
    random_state=0,
    n_jobs=6
)

# imputer hast to fit_transform prior to transform.
# Then, it can be used for the prediction.
# #
p_mdl.fit(X_train, y_train)
imputer.fit_transform(X_train)
xval = imputer.transform(X_train)

p = p_mdl.predict(xval)
p_mdl_mape = mean_absolute_error(y_train, p)
c_mse = 100-p_mdl_mape
print ("Prediction Set Mean Absolute Error Rate: %.2f" % p_mdl_mape)
print ("Prediction Set Mean Absolute Accuracy Rate: %.2f" % c_mse)

# Predicted Results
# #
print ("Predicted 3 Day Results:")
for i in range (3):
    print ( "%.2f" % p[i] )

# Extracting the model to csv file.
# That way it can be graphed via Excel or
# another program.
# #

#a_lines_to_file = ""
#b_lines_to_file = ""

# Exporting Training Set Predictions
#for i in range (len(y_train)):
 #   a_lines_to_file += str(y_train[i])+","+str(x_train_tofile[i])+"\n"

#with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\y_train_out.csv","a+") as file1:
 #   file1.write(str(a_lines_to_file))

# Exporting Test Set Preddictions
#for i in range (len(y_test)):
 #   b_lines_to_file += str(y_test[i])+","+str(x_test_tofile[i])+"\n"

#with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\y_test_out.csv","a+") as file2:
#   file2.write(str(b_lines_to_file))

# Exporting Predictions. Change range head length.
#for i in range (3):
#   a_lines_to_file += str(p[i])+","+str(y_train[i])+"\n"

#with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\predict_col.csv","a+") as file1:
#  file1.write(str(a_lines_to_file))