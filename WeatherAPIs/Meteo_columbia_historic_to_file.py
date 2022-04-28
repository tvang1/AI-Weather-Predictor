#!/usr/local/bin/python
import http.client,json

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
     'x-rapidapi-host': "meteostat.p.rapidapi.com",
     'x-rapidapi-key': "b289fc32bamshc0387fa61b3735cp1f96d7jsn9d169c08ecdc"
     }

# Be sure to change the dates for correct historical data.

conn.request("GET", "/stations/daily?station=72310&start=2022-04-15&end=2022-04-16", headers=headers)
#conn.request("GET", "/stations/daily?station=72310&start=2022-02-21&end=2022-02-22", headers=headers)

res = conn.getresponse()
a_json = res.read().decode()

a_data= json.loads(a_json)

lines_to_file = ""
num_of_lines = 0

for line in a_data['data']:
    num_of_lines +=1

for i in range (num_of_lines):
    lines_to_file += str(a_data['data'][i]['date'])+","+str( ( ((a_data['data'][i]['tavg'])*(9/5))+32) )+","+str(a_data['data'][i]["pres"])+",N/A,"+str(a_data['data'][i]["wspd"])+","+str(a_data['data'][i]["wdir"])+"\n"

with open(r"D:\College\IFT 401 and 402\ASU-CapWeather\WeatherAPIs\API Outputs\columbia_data_02.csv","a+") as file1:
  file1.write(str(lines_to_file))