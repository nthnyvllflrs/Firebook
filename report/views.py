from django.shortcuts import render

from .forms import *


def report_create(request):
  if request.method == 'POST':
    form = ReportForm(request.POST)
    if form.is_valid():
      report = form.save(commit=False)
      report.reporter = request.user
      report.save()
  form = ReportForm()
  return render(request, 'report/report-create.html', {'form': form})