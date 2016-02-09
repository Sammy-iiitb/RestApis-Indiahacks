import urllib2
import json
import sys


def waypoints(src, dst):
 	base = "https://maps.googleapis.com/maps/api/directions/json?"
 	location = "origin="+str(src[0])+","+str(src[1])+"&destination="+str(dst[0]) + "," + str(dst[1])
 	key = "&key=youapikey"
 	url = base+location+key
 	response = urllib2.urlopen(url)
	data = json.load(response)
	print url
	#print data
	tmp = data["routes"][0]["overview_polyline"]["points"]

	print tmp

waypoints([12.9817447954723,77.574481312945], [12.9899747663903,77.572098665973])
