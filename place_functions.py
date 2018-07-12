import googlemaps
from datetime import datetime

# API key shouldn't be stored in code. Move to environment variable. 
gmaps = googlemaps.Client(key='AIzaSyC94G_D29MnwKOepVNsTOqfu99PYtlcuAU')

# Geocoding an address 
geocode_result = gmaps.geocode('161 Camelia Lane, Walnut Creek, Ca')

now = datetime.now()
directions_results = gmaps.directions("161 Camelia Lane", "UCLA", mode="transit", departure_time=now)
print(directions_results)
