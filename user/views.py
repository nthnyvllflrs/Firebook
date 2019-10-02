from django.contrib.auth import update_session_auth_hash # Change Password
from django.contrib.auth.decorators import login_required # Decorator
from django.contrib.auth.forms import PasswordChangeForm # Change Password
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Sum
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .utils import *

from .models import Notification, Reporter, Responder, Fighter
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
      Reporter.objects.create(
        user=user,
        latitude=6.9214,
        longitude=122.0790,
        address='Veterans Ave, Zamboanga, Zamboanga del Sur, Philippines',
      )

      # send_reporter_welcome_email(user)

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
        display_name = form.cleaned_data.get('display_name'),
        phone_number = form.cleaned_data.get('phone_number'),
        station = form.cleaned_data.get('station'),
        latitude = form.cleaned_data.get('latitude'),
        longitude = form.cleaned_data.get('longitude'),
        address = form.cleaned_data.get('address'),
      )

      # send_responder_welcome_email(user)

      account_created = True
  else:
    form = ResponderForm(initial={
        'latitude': 6.9214,
        'longitude': 122.0790,
        'address': 'Veterans Ave, Zamboanga, Zamboanga del Sur, Philippines',
      })
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
  _verifies = Report.objects.filter(reporter=_object).annotate(Count("verifies")).aggregate(Sum("verifies__count"))
  _object_list = Report.objects.filter(reporter=_object).order_by('-timestamp')
  return render(request, 'user/reporter-profile.html', {'object': _object, 'verifies': _verifies , 'object_list': _object_list})

@login_required
def responder_detail(request, username):

  is_reporter = Reporter.objects.filter(user=request.user).exists()
  if is_reporter and not request.user.reporter.activated:
    return redirect('report:report-timeline')

  _object = get_object_or_404(User, username=username)
  # _object_list = Report.objects.filter(verifies=_object).order_by('-timestamp')
  _object_list = Report.objects.filter(responder=_object).order_by('-timestamp')
  paginator = Paginator(_object_list, 3) # Show 3 Reports per page
  page = request.GET.get('page')
  _object_list = paginator.get_page(page)

  _object_list_2 = Fighter.objects.filter(responder=request.user.responder)
  
  return render(request, 'user/responder-profile.html', {'object': _object, 'object_list': _object_list, 'object_list_2': _object_list_2})

@login_required
def notifications(request):
  Notification.objects.filter(recipient=request.user).update(viewed=True)
  object_list = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
  return render(request, 'user/responder-notifications.html', {'object_list': object_list})

@login_required
def responder_notifications_alerts(request):
  object_list = Notification.objects.filter(recipient=request.user, viewed=False).order_by('-timestamp')
  return render(request, 'snippets/notifications.html', {'object_list': object_list})

@login_required
def responder_fighter_creation(request, username):

  if not Responder.objects.filter(user=request.user).exists():
    return redirect('report:report-timeline')

  if request.method == 'POST':
    form = FighterForm(request.POST)
    if form.is_valid():
      fighter = form.save(commit=False)
      fighter.responder = request.user.responder
      fighter.save()

      account_created = True
  else:
    form = FighterForm()
    account_created = False

  return render(request, 'user/responder-fighter-creation.html', {'form': form, 'account_created': account_created})

@login_required
def responder_fighter_deletion(request, username, pk):

  if not Responder.objects.filter(user=request.user).exists():
    return redirect('report:report-timeline')

  _object = get_object_or_404(Fighter, pk=pk)
  _object.delete()

  return redirect('user:responder-detail', request.user.responder)