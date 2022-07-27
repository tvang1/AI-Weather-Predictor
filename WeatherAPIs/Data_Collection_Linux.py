#!\bin\bash
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
        if (city=="castlerock" and state=="colorado"):
            with open(r"/mnt/d/GitRepositories/Simple-Weather-Predictor/WeatherAPIs/API Outputs/castle_rock_data.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")

        elif (city=="denver" and state=="colorado"):
            with open(r"/mnt/d/GitRepositories/Simple-Weather-Predictor/WeatherAPIs/API Outputs/denver_data.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")
            
        elif (city=="boulder" and state=="colorado"):
            with open(r"/mnt/d/GitRepositories/Simple-Weather-Predictor/WeatherAPIs/API Outputs/boulder_data.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")

    except:
        print ("An error log was saved to the API Outputs directory.")
        with open(r"/mnt/d/GitRepositories/Simple-Weather-Predictor/WeatherAPIs/API Outputs/error_log.csv","w+") as file1:
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
        if (zip=="80108"):
            with open(r"/mnt/d/GitRepositories/Simple-Weather-Predictor/WeatherAPIs/API Outputs/castle_rock_data.csv","a+") as file1:
                file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")

        elif (zip=="80249"):
            with open(r"/mnt/d/GitRepositories/Simple-Weather-Predictor/WeatherAPIs/API Outputs/denver_data.csv","a+") as file1:
              file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")
            
        elif (zip=="80304"):
            with open(r"/mnt/d/GitRepositories/Simple-Weather-Predictor/WeatherAPIs/API Outputs/boulder_data.csv","a+") as file1:
              file1.write(str(lines_to_file)+"\n")
            print ("Added to file successfully.")

    except:
        print ("An error log was saved to the API Outputs directory.")
        with open(r"/mnt/d/GitRepositories/Simple-Weather-Predictor/WeatherAPIs/API Outputs/error_log.csv","w+") as file1:
           file1.write(sys.sys.exc_info())
    
# Driver
# #

# Please alter the "date" for data to be accurate.
# #

date = "2022-07-26"

open_weather_api = "8c239ac62ba042b490fb460648e3c15b"

weather_api = "a0c11aef091643ba8a1180136222001"

cr_zip = "80108"
denver_zip = "80249"
boulder_zip = "80304"

get_open_weather(open_weather_api,date,"castlerock","colorado")
get_open_weather(open_weather_api,date,"denver","colorado")
get_open_weather(open_weather_api,date,"boulder","colorado")
get_weather_api(weather_api,date,cr_zip)
get_weather_api(weather_api,date,denver_zip)
get_weather_api(weather_api,date,boulder_zip)
