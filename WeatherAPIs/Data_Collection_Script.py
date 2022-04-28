#!/bin/bash
import urllib.request, json, sys

# Functions
# 
# These are functions for the data collection
# of APIs. This is done to automate the collection
# proccess and to improve more efficient data
# collection for the machine learning algorithm.
# #

# OpenWeatherMap API allows returns daily forecasts.
# 
# It allows for 60 requests per minute that will display
# hourly forecasts for the current day.
# 
# It stores the results to 'a_dict' in JSon format
# where the 'lines_to_file' will write the data
# that is specified for inputing later.
# #

def get_open_weather(api,date,city,state):

    a_dict = {}
    lines_to_file = ""

    a_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+","+state+"&units=imperial&mode=json&appid="+api
    connection1 = urllib.request.urlopen(a_url)
    responseString = connection1.read().decode()

    a_dict = json.loads(responseString)
    lines_to_file = ( str(date)+","+str(a_dict['main']['temp'])+","+str(a_dict['main']['pressure'])+","+str(a_dict['weather'][0]['description'])+","+str(a_dict['wind']['speed'])+","+str(a_dict['wind']['deg']) )

    try: 
        if (city=="charlotte" and state=="northcarolina"):
            with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\charlotte_data_02.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")

        elif (city=="atlanta" and state=="georgia"):
            with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\atlanta_data_02.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")
            

        elif (city=="columbia" and state=="southcarolina"):
            with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\columbia_data_02.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")

    except:
        print ("An error log was saved to the API Outputs directory.")
        with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\error_log.csv","w+") as file1:
            file1.write(sys.sys.exc_info())

# WeatherAPI stores the results to 'a_dict' in JSon format
# where the 'lines_to_file' will write the data
# that is specified for inputing later.
# #

def get_weather_api(api, date, zip):
    
    a_dict = {}
    lines_to_file = ""

    a_url = "http://api.weatherapi.com/v1/current.json?key="+api+"&q="+zip+"&aqi=no"
    connection1 = urllib.request.urlopen(a_url)
    responseString = connection1.read().decode()

    a_dict = json.loads(responseString)
    lines_to_file = ( str(date)+","+str(a_dict['current']['temp_f'])+","+str(a_dict['current']['pressure_mb'])+","+str(a_dict['current']['condition']['text'])+","+str(a_dict['current']['wind_mph'])+","+str(a_dict['current']['wind_degree']) )

    try: 
        if (zip=="28208"):
            with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\charlotte_data_02.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")

        elif (zip=="30320"):
            with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\atlanta_data_02.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")
            
        elif (zip=="29170"):
            with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\columbia_data_02.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")

    except:
        print ("An error log was saved to the API Outputs directory.")
        with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\error_log.csv","w+") as file1:
            file1.write(sys.sys.exc_info())
    
# Driver
# #

# Please alter the "date" for data to be accurate.
# #

date = "2022-04-24"

open_weather_api = "8c239ac62ba042b490fb460648e3c15b"

weather_api = "a0c11aef091643ba8a1180136222001"
atl_zip = "30320"
chrtte_zip = "28208"
colum_zip = "29170"

get_open_weather(open_weather_api,date,"charlotte","northcarolina")
get_open_weather(open_weather_api,date,"atlanta","georgia")
get_open_weather(open_weather_api,date,"columbia","southcarolina")
get_weather_api(weather_api,date,atl_zip)
get_weather_api(weather_api,date,chrtte_zip)
get_weather_api(weather_api,date,colum_zip)