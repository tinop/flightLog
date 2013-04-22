# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from flights.models import Flight

def home2(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def home(request):
	entries = Flight.objects.all()[:10]
	return render_to_response('index.html',{'Flights' : entries})
# return render_to_response('index.html')