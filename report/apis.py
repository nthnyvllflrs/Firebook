from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Report
from user.models import Notification

@api_view(['GET'])
def report_verify_toggle(request, pk):
  obj = get_object_or_404(Report, id=pk)
  user = request.user

  updated, verified = False, False 

  if user.is_authenticated:
    if user in obj.verifies.all():
      verified = False
      obj.verifies.remove(user)
    else:
      verified = True
      obj.verifies.add(user)
      updated = True

  data = {
    'updated': updated,
    'verified': verified
  }

  return Response(data)

@api_view(['GET'])
def report_status_toggle(request, pk):
  obj = get_object_or_404(Report, id=pk)
  user = request.user

  if user.is_authenticated:
    obj.status = "Cleared"
    obj.save()

  data = {
    'updated': True,
  }

  return Response(data)

@api_view(['GET'])
def report_respond(request, pk):
  obj = get_object_or_404(Report, id=pk)
  user = request.user

  updated, responding = False, False 

  if user.is_authenticated:
    if user in obj.responder.all():
      responding = False
      obj.responder.remove(user)
    else:
      responding = True
      obj.responder.add(user)
      updated = True

  Notification.objects.create(sender=request.user, recipient=obj.reporter, report=obj, title='Responder Responding')

  data = {
    'updated': updated,
    'responding': responding
  }

  return Response(data)