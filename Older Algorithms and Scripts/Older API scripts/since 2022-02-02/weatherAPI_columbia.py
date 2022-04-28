#!/usr/local/bin/python
import urllib.request, json

# It stores the results to 'a_dict' in JSon format
# where the 'lines_to_file' will write the data
# that is specified for inputing later.
# 
# Change date to current day.
# #

date = "2022-01-31"
zip = "29170"
api = "a0c11aef091643ba8a1180136222001"

a_dict = {}
lines_to_file = ""


open_weatherURL = "http://api.weatherapi.com/v1/current.json?key="+api+"&q="+zip+"&aqi=no"
connection1 = urllib.request.urlopen(open_weatherURL)
responseString = connection1.read().decode()

a_dict = json.loads(responseString)

lines_to_file = ( str(date)+","+str(a_dict['current']['temp_f']) )

# Please change file path to match your directory:
#   r"{Your file path}\ASU-CapWeather\WeatherAPIs\API Outputs\openWeather_001.csv"
#
# with open(r"C:\Users\Pecha Berry\Desktop\ASU-CapWeather\WeatherAPIs\API Outputs\charlotte_data.csv","a") as file1:
#    file1.write(str(lines_to_file)+"\n")

with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\columbia_data.csv","a") as file1:
    file1.write(str(lines_to_file)+"\n")