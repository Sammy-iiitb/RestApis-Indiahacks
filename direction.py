import googlemaps
gmaps = googlemaps.Client(key='Your api key')

# Geocoding an address
geocode_result = gmaps.geocode('majestic bus stand, india')
print geocode_result

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
#now = datetime.now()
