from django.db import models

# Create your models here.
class Flight(models.Model):
    date = models.DateTimeField('date published')
    fromAirport = models.CharField(max_length=4)
    toAirport = models.CharField(max_length=4)
    
