# Create your views here.
import django.shortcuts
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the poll index.")
    
    
def flightlog(request):
  return django.shortcuts.render(request,
    'flights/matchlog.html',
    {'games_list' : 'a',
    'players_query_prefix' : 'a',
    'page_query_suffix' : 'a',
    'ranking_query' : 'a',
    'displayed_pages' : 'a',
    'date_title' : 'a',
    'opponents_title' : 'a'})