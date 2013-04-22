from django.contrib import admin

from flights.models import Flight,Aircraft,Pilot

admin.site.register(Pilot)
admin.site.register(Aircraft)
admin.site.register(Flight)
