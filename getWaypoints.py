import urllib2
import json
import sys

def waypoints(src, dst):
 	base = "https://maps.googleapis.com/maps/api/directions/json?"
 	location = "origin="+str(src[0])+","+str(src[1])+"&destination="+str(dst[0]) + "," + str(dst[1])+"&mode=transit"
 	key = "&key=yourapikey"
 	url = base+location+key
 	response = urllib2.urlopen(url)
	data = json.load(response)
	print url
	#print data
	distance = data["routes"][0]["legs"][0]["distance"]["text"]
	duration = data["routes"][0]["legs"][0]["duration"]["text"]
	#bus = data["routes"][0]["legs"][0]["steps"][0]["steps"][0]["transit_details"]["line"]["sho
	print "distance : "+ distance
	print "duration : "+ duration
	return distance, duration
	#tmp = data["routes"][0]["overview_polyline"]["points"]

	#print decodeGMapPolylineEncoding(tmp)

waypoints([sys.argv[1],sys.argv[2]], [sys.argv[3],sys.argv[4]])
#waypoints([12.9817447954723,77.574481312945], [12.9899747663903,77.572098665973])
#whitefield: 12.971289, 77.750098
#silk board: 12.917630, 77.623379
#iiitb: 12.8446784,77.6610528
#majestic: 12.9773452,77.566781
