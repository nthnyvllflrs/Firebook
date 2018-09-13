from django.contrib.auth import update_session_auth_hash # Change Password
from django.contrib.auth.forms import PasswordChangeForm # Change Password
from django.shortcuts import render, get_object_or_404


from .forms import *
from report.models import Report


def reporter_signup(request):
  if request.method == 'POST':
    form = ReporterForm(request.POST)
    if form.is_valid():
      form.save()
      user = User.objects.get(username=form.cleaned_data.get('username'))
      Reporter.objects.create(user=user)
  form = ReporterForm()
  return render(request, 'user/reporter-signup.html', {'form': form,})


def responder_signup(request):
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
  form = ResponderForm()
  return render(request, 'user/responder-signup.html', {'form': form,})


def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
  form = PasswordChangeForm(request.user)
  return render(request, 'user/user-change-password.html', {'form': form,})


def reporter_detail(request, username):
  _object = get_object_or_404(User, username=username)
  _object_list = Report.objects.filter(reporter=_object).order_by('-timestamp')
  return render(request, 'user/reporter-profile.html', {'object': _object, 'object_list': _object_list})


def responder_detail(request, username):
  _object = get_object_or_404(User, username=username)
  _object_list = Report.objects.filter(verifies=_object).order_by('-timestamp')
  return render(request, 'user/responder-profile.html', {'object': _object, 'object_list': _object_list})