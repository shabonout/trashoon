from django.shortcuts import render

# Create your views here.
from .models import Pin

def jsontodb(request):
	#Grabbing the data from the JSON file
	import json
	from .models import Pin
	from django.http import HttpResponse
	
	if request.GET.get('file'):
		filename = request.GET['file'];

		json_data = open('utils/json_pins/'+filename+'.json')   
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
	return HttpResponse(request, "<html>Database changed</html>")

def pins_view(request): # the request means: whenever someone goes to the URL
	pin_objects = Pin.objects.all() # here we are grabbing every object
	nobjects = pin_objects.count()
	context = { 
	# Putting the objects into a context
	# Context dictionary with 'KEY': VALUE
		'pin_objects': pin_objects,
		'nobjects': nobjects
	}
	return render(request, "WebPage.html", context) # Render function to render the page

