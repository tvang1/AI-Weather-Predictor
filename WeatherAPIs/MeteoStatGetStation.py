#!/usr/local/bin/python
import http.client

# This code was generated from the https://rapidapi.com/meteostat/api/meteostat/
# 
# The website is accessible from Thomas Vang's ASU gmail but the code should still
# work as long as the 'lat' and 'lon' are changed in the request.
# Use "https://www.latlong.net/" to look up locations. 
# #

conn = http.client.HTTPSConnection("meteostat.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "meteostat.p.rapidapi.com",
    'x-rapidapi-key': "b289fc32bamshc0387fa61b3735cp1f96d7jsn9d169c08ecdc"
    }

# Replace the values for 'lat' and 'lon' for the searchable location.
# 
# Upon results, copy and paste desired 'id' tuple to the 'MeteoStaions.txt'
# #

conn.request("GET", "/stations/nearby?lat=33.836082&lon=-81.163727", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))