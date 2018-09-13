from django.shortcuts import render

from report.models import Report
from user.models import Responder

def landing(request):

  object_list = Report.objects.order_by('-timestamp')[:3]
  stations = {
    'fire': Responder.objects.filter(station='Fire').count() ,
    'crime': Responder.objects.filter(station='Crime').count() 
  }

  return render(request, 'index.html', {'object_list': object_list, 'stations': stations})


def responders(request):
  
  context = {
    'fire_stations': Responder.objects.filter(station='Fire'),
    'police_stations': Responder.objects.filter(station='Crime'),
  }

  return render(request, 'responders.html', {'context': context})