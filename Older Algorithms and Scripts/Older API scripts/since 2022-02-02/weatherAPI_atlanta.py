#!/usr/local/bin/python
import urllib.request, json

from pyparsing import line

# It stores the results to 'a_dict' in JSon format
# where the 'lines_to_file' will write the data
# that is specified for inputing later.
# 
# Change date to current day.
# #

date = "2022-01-31"
zip = "30320"
api = "a0c11aef091643ba8a1180136222001"

a_dict = {}
lines_to_file = ""


open_weatherURL = "http://api.weatherapi.com/v1/current.json?key="+api+"&q="+zip+"&aqi=no"
connection1 = urllib.request.urlopen(open_weatherURL)
responseString = connection1.read().decode()

a_dict = json.loads(responseString)

#print (a_dict)

print ("date,temperature,pressure,pattern,wind_speed,wind_degree")
lines_to_file = ( str(date)+","+str(a_dict['current']['temp_f'])+","+str(a_dict['current']['pressure_mb'])+","+str(a_dict['current']['condition']['text'])+","+str(a_dict['current']['wind_mph'])+","+str(a_dict['current']['wind_degree']) )
print (lines_to_file)

# Please change file path to match your directory:
#   r"{Your file path}\ASU-CapWeather\WeatherAPIs\API Outputs\openWeather_001.csv"
#
# with open(r"C:\Users\Pecha Berry\Desktop\ASU-CapWeather\WeatherAPIs\API Outputs\charlotte_data.csv","a") as file1:
#    file1.write(str(lines_to_file)+"\n")

#with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\atlanta_data.csv","a") as file1:
   # file1.write(str(lines_to_file)+"\n")