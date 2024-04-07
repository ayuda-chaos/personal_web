#Small project by Aayush Timalsina.
#The code written below track your location, service provider, your langitude and lalitude
# For this i have get help from python org and opencagedata.com

import phonenumbers
#For tracking  location
import folium
# I have import geocoder as well as carrier in advanced for tracking
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
number = input("please enter a phone number (in international format): ")
number_track = phonenumbers.parse(number)
location_str = geocoder.description_for_number(number_track, "en")
print(location_str)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

key = "b519060a670f4421993f91d56485a0e8"
geocoder = OpenCageGeocode(key)
query = str(location_str)
result = geocoder.geocode(query)
lat = result[0]["geometry"]["lat"]
lng = result[0]["geometry"]["lng"]
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location_str).add_to(myMap)
myMap.save("mylocation.html")
