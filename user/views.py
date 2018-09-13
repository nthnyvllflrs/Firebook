from django.contrib.auth import update_session_auth_hash # Change Password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm # Change Password
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from report.models import Report


def reporter_signup(request):
  if request.user.is_authenticated:
    return redirect('report:report-timeline')

  account_created = False
  if request.method == 'POST':
    form = ReporterForm(request.POST)
    if form.is_valid():
      form.save()
      user = User.objects.get(username=form.cleaned_data.get('username'))
      Reporter.objects.create(user=user)
      account_created = True
  else:
    form = ReporterForm()
  return render(request, 'user/reporter-signup.html', {'form': form, 'account_created': account_created})

@login_required
def responder_signup(request):

  if not request.user.is_superuser:
    return redirect('report:report-timeline')

  account_created = False
  if request.method == 'POST':
    form = ResponderForm(request.POST)
    if form.is_valid():
      form.save()
      user = User.objects.get(username=form.cleaned_data.get('username'))
      Responder.objects.create(
        user=user,
        phone_number = form.cleaned_data.get('phone_number'),
        station = form.cleaned_data.get('station'),
        latitude = form.cleaned_data.get('latitude'),
        longitude = form.cleaned_data.get('longitude'),
        address = form.cleaned_data.get('address'),
      )
      account_created = True
  else:
    form = ResponderForm()
  return render(request, 'user/responder-signup.html', {'form': form, 'account_created': account_created})

@login_required
def change_password(request):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter and not request.user.reporter.activated:
    return redirect('report:report-timeline')

  password_updated = False
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      password_updated = True
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'user/user-change-password.html', {'form': form, 'password_updated': password_updated})

@login_required
def reporter_detail(request, username):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter and not request.user.reporter.activated:
    return redirect('report:report-timeline')

  _object = get_object_or_404(User, username=username)
  _object_list = Report.objects.filter(reporter=_object).order_by('-timestamp')
  return render(request, 'user/reporter-profile.html', {'object': _object, 'object_list': _object_list})

@login_required
def responder_detail(request, username):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter and not request.user.reporter.activated:
    return redirect('report:report-timeline')

  _object = get_object_or_404(User, username=username)
  _object_list = Report.objects.filter(verifies=_object).order_by('-timestamp')
  return render(request, 'user/responder-profile.html', {'object': _object, 'object_list': _object_list})

@login_required
def reporter_location(request):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter and not request.user.reporter.activated:
    return redirect('report:report-timeline')

  if request.method == 'POST':
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    address = request.POST['address']

    user = User.objects.get(username=request.user)
    reporter = Reporter.objects.get(user=user)
    reporter.latitude = latitude
    reporter.longitude = longitude
    reporter.address = address
    reporter.save()
  return redirect('report:report-timeline')