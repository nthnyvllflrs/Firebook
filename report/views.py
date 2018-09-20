import geocoder

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .utils import nearby_responder
from user.models import Reporter

@login_required
def report_create(request):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter and not request.user.reporter.activated:
    return redirect('report:report-timeline')

  if is_reporter:
    report_created, can_report = False, False
    time_threshold = datetime.now() - timedelta(minutes=5)
    reports = Report.objects.filter(reporter=request.user, timestamp__gte=time_threshold).order_by('-timestamp')
    results = Report.objects.filter(timestamp__gte=time_threshold).exclude(verifies=request.user).order_by('-timestamp')

    if not reports:
      can_report = True
    else:
      can_report = False

    if request.method == 'POST':
      form = ReportForm(request.POST)
      if form.is_valid():
        report = form.save(commit=False)
        report.reporter = request.user

        # Reverse GeoCoding
        latitude = float(report.latitude)
        longitude = float(report.longitude)
        location = geocoder.google([latitude, longitude], method='reverse', key=settings.GOOGLE_MAP_API_KEY)
        report.address = location.address

        nearby_responder(report)
        report.save()
        
        report_created = True
    else:
      form = ReportForm(initial={
        'latitude': request.user.reporter.latitude,
        'longitude': request.user.reporter.longitude,
        'address': request.user.reporter.address,
      })

    context = {
      'form': form, 
      'report_created': report_created, 
      'can_report': can_report, 
      'results': results
    }

    return render(request, 'report/report-create.html', context) 
  else:
    return redirect('report:report-timeline')

@login_required
def report_timeline(request):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter and not request.user.reporter.activated:
    account_active = False
  else:
    account_active = True

  if account_active:
    object_list = Report.objects.order_by('-timestamp')

    if request.is_ajax():
      return render(request, 'report/report-timeline-ajax.html', {'object_list': object_list})

    return render(request, 'report/report-timeline.html', {'account_active': account_active, 'object_list': object_list})
  
  return render(request,'report/report-timeline.html', {'account_active': account_active})

@login_required
def report_dashboard(request):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter:
    return redirect('report:report-timeline')

  station = request.user.responder.station
  object_list = Report.objects.filter(emergency=station).order_by('-timestamp')

  if request.is_ajax():
      return render(request, 'report/report-dashboard-ajax.html', {'object_list': object_list})

  return render(request, 'report/report-dashboard.html', {'object_list': object_list})

@login_required
def report_detail(request, pk):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter and not request.user.reporter.activated:
    return redirect('report:report-timeline')

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  _object = get_object_or_404(Report, pk=pk)

  if is_reporter or request.user.is_superuser:
    return render(request, 'report/report-detail-reporter.html', {'object': _object})
  else:
    return render(request, 'report/report-detail-responder.html', {'object': _object})
