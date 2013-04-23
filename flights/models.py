from django.db import models

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
   first_name = models.CharField(max_length=15)
   last_name = models.CharField(max_length=15)
       
   def __unicode__(self):
       return self.first_name + " " +self.last_name

class Flight(models.Model):
   aircraft = models.ForeignKey(Aircraft)
   date = models.DateField()
   fromAirport = models.CharField(max_length=4)
   toAirport = models.CharField(max_length=4)
   departure_time = models.TimeField()
   arrival_time = models.TimeField()
   pic = models.ForeignKey(Pilot)
   landings = models.PositiveIntegerField()
   remark = models.TextField()
    
   def __unicode__(self):
       return self.fromAirport