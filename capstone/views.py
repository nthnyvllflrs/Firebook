from django.shortcuts import render, redirect

from report.models import Report
from user.models import Responder

def landing(request):

  if request.user.is_authenticated:
    if Responder.objects.filter(user=request.user).exists():
      return redirect('report:report-timeline')
    else:
      return redirect('report:report-timeline')

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