#!/usr/local/bin/python
import urllib.request, json

# This is the National Weather Service API
# 
# gov_weatherURL1 displays the current forecast based on 'lat',
# then 'lon'. Will display results in a link in
# JSon format.
# Use "https://www.latlong.net/" to look up locations.
# 
# gov_weqatherURL2 has the emergency data. It has to go through
# some formatting prior to extracting data manually.
# #

a_dict1 = {}
a_dict2 = {}

lines_to_file = ""

# Atlanta
# #
#gov_weatherURL1 = "https://api.weather.gov/points/33.7490,-84.3880"
#gov_weatherURL2 = "https://api.weather.gov/alerts/active?area=GA"

# Columbia
# #
#gov_weatherURL1 = "https://api.weather.gov/points/34.007,-81.0348"
#gov_weatherURL2 = "https://api.weather.gov/alerts/active?area=SC"

# Charlotte
# #
gov_weatherURL1 = "https://api.weather.gov/points/33.2271,-80.8431"
gov_weatherURL2 = "https://api.weather.gov/alerts/active?area=NC"

connection1 = urllib.request.urlopen(gov_weatherURL1)
connection2 = urllib.request.urlopen(gov_weatherURL2)
responseString1 = connection1.read().decode()
responseString2 = connection2.read().decode()

a_dict1 = json.loads(responseString1)
a_dict2 = json.loads(responseString2)

# Results are in a link. Use link to
# find data.
# #
print ( "Link to forecasts: "+"\n"+str(a_dict1['properties']['forecast']) )

# With Emergency Viewing, the code will output it to an appropriate 
# location as a json file. The file output is not formatted correctly,
# so it needs to be copied into a formatter/correcter and copied back
# to the weather_gov_formated.json to be viewed correctly.
# #
lines_to_file += str(a_dict2)
with open(r"D:\GitRepositories\Simple-Weather-Predictor\WeatherAPIs\API Outputs\weather_gov.json","w+") as file1:
    file1.write(str(lines_to_file)+"\n")
    print ("\nAdded to file successfully.") 
    print ("Use a Json formatter to propperly format file for appropriate\nviewing emergency events.\nGo to \"https://jsonformatter.curiousconcept.com/\" to paste file contents there.\n")