from django.db import models

# Create your models here.

class Pin(models.Model):
	title = models.CharField(max_length=120)
	imgurl = models.TextField()
	website = models.TextField()
	description = models.TextField()
	latitude = models.DecimalField(decimal_places=7,max_digits=10)
	longitude = models.DecimalField(decimal_places=7,max_digits=10)
	date = models.DateField()

	# author = models.CharField(max_lenghr=100) # an example of another field
	def __str__(self):
		return self.title