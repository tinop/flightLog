# Create your views here.
import django.shortcuts
from django.http import HttpResponse
import flights.models as M

def home(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    return django.shortcuts.render(request, 'flights/index.html')
    
    
def flightlog(request):
  flights = M.Flight.objects.all()
  return django.shortcuts.render(request,
    'flights/flightList.html',
    {'games_list' : 'a',
    'players_query_prefix' : 'a',
    'page_query_suffix' : 'a',
    'ranking_query' : 'a',
    'displayed_pages' : 'a',
    'date_title' : 'a',
    'opponents_title' : 'a',
    'flights': flights})