import urllib2
import json
import sys

def waypoints(src):
 	base = "https://maps.googleapis.com/maps/api/geocode/json?"
 	location = "address="+str(src)
 	key = "&key=yourapikey"
 	url = base+location+key
 	response = urllib2.urlopen(url)
	data = json.load(response)
	print url
	print data["results"][0]["geometry"]["location"]
	#print data
	#distance = data["routes"][0]["legs"][0]["distance"]["text"]
	#duration = data["routes"][0]["legs"][0]["duration"]["text"]
	#bus = data["routes"][0]["legs"][0]["steps"][0]["steps"][0]["transit_details"]["line"]["sho
	#print "distance : "+ distance
	#print "duration : "+ duration
	#tmp = data["routes"][0]["overview_polyline"]["points"]

	#print decodeGMapPolylineEncoding(tmp)

waypoints(sys.argv[1])
#https://maps.googleapis.com/maps/api/geocode/json?address=iiit bangalore&key=AIzaSyBfUX2fWpOzRE779sepxJW3VJ0Ho2b0lIw
