#!/usr/local/bin/python
import http.client,json
from warnings import catch_warnings

# This uses the MetoStation API to get past data. 
# There can pnly be 300 requests a month.
# 
# Refer to the "MeteoStation Data Dump Example.json"
# to gather more specified data.
# 
# This file will look through the request json format
# and export those contents to the correct historical
# csv file for data comparison.
# #

a_data= {}

conn = http.client.HTTPSConnection("meteostat.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "b289fc32bamshc0387fa61b3735cp1f96d7jsn9d169c08ecdc",
    'X-RapidAPI-Host': "meteostat.p.rapidapi.com"
    }

# Be sure to change the dates for correct historical data.

a_date = "2022-12-22&end=2022-12-25"

conn.request("GET", "/stations/daily?station=KBDU0&start="+a_date, headers=headers)

res = conn.getresponse()
a_json = res.read().decode()

a_data= json.loads(a_json)

lines_to_file = ""
num_of_lines = 0
line_placeholder = "####"

for line in a_data['data']:
    num_of_lines +=1

for i in range (num_of_lines):
    try:
        lines_to_file += str(str(line_placeholder)+","+a_data['data'][i]['date'])+","+str( ( ((a_data['data'][i]['tavg'])*(9/5))+32) )+","+str(a_data['data'][i]["pres"])+",None,"+str(a_data['data'][i]["wspd"])+","+str(a_data['data'][i]["wdir"])+"\n"
    except:
        lines_to_file += str(str(line_placeholder)+","+a_data['data'][i]['date'])+",None,"+str(a_data['data'][i]["pres"])+",None,"+str(a_data['data'][i]["wspd"])+","+str(a_data['data'][i]["wdir"])+"\n"
    

#print ("date,temperature,pressure,pattern,wind_speed,wind_degree")

with open(r"D:\GitRepositories\Simple-Weather-Predictor\WeatherAPIs\API Outputs\boulder_data.csv","a+") as file1:
  file1.write(str(lines_to_file))