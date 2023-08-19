
'''
Phone number tracker

Created by *Abdullah EL-Yamani*
-----------------------------
Link Youtube Video => https://youtu.be/Geisa_ib5hs
Youtube Channel => Sam Codes
'''

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
import folium


number = "+919865122122" # +CodeCountry PhoneNumber

key = "e8bae35e539e41fd9a645d2e188a29cf" # From =>  https://opencagedata.com/dashboard#geocoding > API Keys


san_num = phonenumbers.parse(number)

your_location = geocoder.description_for_number(san_num, "en")

print("Country Name => ", your_location)
print("----------------------\n")

# get service provider

service_provider = phonenumbers.parse(number)

telecom_company =  carrier.name_for_number(service_provider, "en")

print("Telecom Company Name => ", telecom_company)
print("---------------------------------\n")

geocoder = OpenCageGeocode(key)

query = str(your_location)

results = geocoder.geocode(query)

print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print("\n-------------------------------")
print("x =", lat,"  y =", lng)
print("-------------------------------\n")

location = [lat, lng]

Map = folium.Map(location=location, zoom_start=10)

folium.Marker(location, popup = your_location).add_to(Map)

Map.save("loc_map.html")


