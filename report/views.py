from django.shortcuts import render, get_object_or_404

from .forms import *
from user.models import Reporter


def report_create(request):
  if request.method == 'POST':
    form = ReportForm(request.POST)
    if form.is_valid():
      report = form.save(commit=False)
      report.reporter = request.user
      report.save()
  form = ReportForm()
  return render(request, 'report/report-create.html', {'form': form})


def report_timeline(request):
  object_list = Report.objects.order_by('-timestamp')
  return render(request, 'report/report-timeline.html', {'object_list': object_list})


def report_dashboard(request):
  station = request.user.responder.station
  object_list = Report.objects.filter(emergency=station).order_by('-timestamp')
  return render(request, 'report/report-dashboard.html', {'object_list': object_list})


def report_detail(request, pk):
  is_reporter = Reporter.objects.filter(user=request.user).exists()
  _object = get_object_or_404(Report, pk=pk)

  if is_reporter:
    return render(request, 'report/report-detail-reporter.html', {'object': _object})
  else:
    return render(request, 'report/report-detail-responder.html', {'object': _object})