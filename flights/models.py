from django.db import models
import datetime
import time
#from datetime import datetime


# Create your models here.

class Aircraft(models.Model):
   MODELS = (('remosGx', 'Remos GX'),
             ('ch60', 'CH 60'))
   REGISTRATIONS = (('hbwyd','HB-WYD'),
                   ('hbwyf','HB-WYF'),
                    ('hbwyg','HB-WYG'),
                    ('hbykm','HB-YKM'))
   model = models.CharField(max_length=10, choices=MODELS)
   registration = models.CharField(max_length=6, choices=REGISTRATIONS)

   def __unicode__(self):
       return self.get_model_display() + " : " + self.get_registration_display()

       
class Pilot(models.Model):
   name = models.CharField(max_length=15)
       
   def __unicode__(self):
       return self.name

       
       
class Flight(models.Model):

  CHOICES = (('select1','select 1'),
	    ('select2','select 2'))
         
  aircraft = models.ForeignKey(Aircraft)
  date = models.DateField()
  fromAirport = models.CharField(max_length=4, verbose_name='from')
  toAirport = models.CharField(max_length=4, verbose_name='to')
  departure_time = models.TimeField()
  arrival_time = models.DateTimeField()
  pic = models.ForeignKey(Pilot)
  landings = models.PositiveIntegerField()
  night = models.BooleanField(default=False)
  ifr = models.BooleanField(default=False)
  remark = models.TextField()
  #like = models.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    
  def flightTime(self):
    FMT = '%H:%M:%S'
    #t = datetime.strptime(self.arrival_time,'%I:%M').strftime('%H:%M')
    t1 = self.arrival_time.date()
    t2 = self.departure_time
    #t3 = time.mktime(t2) - time.mktime(t1)
    #return t2.strftime('%H:%M:%S')
    return t2
    #return t
  flightTime.short_description = 'Flight Time'
  
  def flightTimex(self):
    #start="10:23:00"
    #dep = time.strptime(self.departure_time,'%I:%M')
    #start_dt = datetime.strptime(start, '%H:%M:%S')
    return self.arrival_time.strftime('%H:%M:%S')
  flightTimex.short_description = 'Flight Timex'
  
  
  def __unicode__(self):
      return self.fromAirport