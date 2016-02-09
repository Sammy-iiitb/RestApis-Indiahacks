import urllib
import json
url_base = "https://maps.googleapis.com/maps/api/directions/json?origin=12.917630,%2077.623379&destination=12.971289,%2077.750098&mode=transit&key=yourapikey"
htmltext = urllib.urlopen(url_base).read()
htmltext = json.loads(htmltext)
#print htmltext["routes"][0]["legs"][0]["steps"][0]["distance"]
"""Here select value range according to you. If you find any modification just let me know"""
i=1
while(i<4):
    print htmltext["routes"][0]["legs"][0]["steps"][i]["transit_details"]["line"]["short_name"]
    i=i+2
