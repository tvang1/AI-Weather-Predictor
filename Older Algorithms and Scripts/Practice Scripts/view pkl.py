import pickle
import pandas as pd
import joblib

a_file_path = "trained_model.csv"
# a_file_path = r"C:\Users\Pecha Berry\Desktop\ASU-CapWeather\trained_model.pkl"

print (joblib.load(a_file_path))