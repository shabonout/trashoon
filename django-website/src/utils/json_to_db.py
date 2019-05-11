#Grabbing the data from the JSON file
import json

from .models import Pin

json_data = open('utils/json_pins/example.json')   
data1 = json.load(json_data)

title = data1['title']
imgurl = data1['imgurl']
website = data1['website']
description = data1['description']
longitude = data1['longitude']
latitude = data1['latitude']
date = data1['date']

json_data.close()

#Putting the data in the database

Pin.objects.all()

j = Pin(title=title,imgurl=imgurl,website=website,description=description,longitude=longitude,latitude=latitude,date=date)

j.save()