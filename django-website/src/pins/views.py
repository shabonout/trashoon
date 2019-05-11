from django.shortcuts import render

# Create your views here.
from .models import Pin

def pins_view(request): # the request means: whenever someone goes to the URL
	pin_objects = Pin.objects.all() # here we are grabbing every object
	context = { 
	# Putting the objects into a context
	# Context dictionary with 'KEY': VALUE
		'pin_objects': pin_objects
	}
	return render(request, "index.html", context) # Render function to render the page

