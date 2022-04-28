#!/usr/local/bin/python
import urllib.request, json

# OpenWeather API allows returns daily forecasts.
# 
# It allows for 60 requests per minute that will display
# hourly forecasts for the current day.
# 
# It stores the results to 'a_dict' in JSon format
# where the 'lines_to_file' will write the data
# that is specified for inputing later.
# 
# Change date to current day.
# #

date = "2022-01-31"
city = "atlanta"
state = "georgia"
api = "8c239ac62ba042b490fb460648e3c15b"

a_dict = {}
lines_to_file = ""

# Example of request
# open_weatherURL = "https://api.openweathermap.org/data/2.5/weather?q={city,state}&units=imperial&mode=json&appid={api key}"
# #

open_weatherURL = "https://api.openweathermap.org/data/2.5/weather?q="+city+","+state+"&units=imperial&mode=json&appid="+api
connection1 = urllib.request.urlopen(open_weatherURL)
responseString = connection1.read().decode()

a_dict = json.loads(responseString)

lines_to_file = ( str(date)+","+str(a_dict['main']['temp']) )

# Please change file path to match your directory:
#   r"{Your file path}\ASU-CapWeather\WeatherAPIs\API Outputs\openWeather_001.csv"
#
# with open(r"C:\Users\Pecha Berry\Desktop\ASU-CapWeather\WeatherAPIs\API Outputs\charlotte_data.csv","a") as file1:
#    file1.write(str(lines_to_file)+"\n")

with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\atlanta_data.csv","a") as file1:
    file1.write(str(lines_to_file)+"\n")