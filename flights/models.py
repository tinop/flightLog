from django.db import models

# Create your models here.
class Fligt(models.Model):
    date = models.DateTimeField('date published')