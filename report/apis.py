from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Report
from .models import Notification

class ReportVerfiyAPIToggle(APIView):

  authentication_classes = (authentication.SessionAuthentication,)
  permission_classes = (permissions.IsAuthenticated,)

  def get(self, request, pk=None, format=None):
    obj = get_object_or_404(Report, id=pk)
    user = self.request.user

    updated = False
    verified = False

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


class NotificationViewedAPI(APIView):

  authentication_classes = (authentication.SessionAuthentication,)
  permission_classes = (permissions.IsAuthenticated,)

  def get(self, request, pk=None, format=None):
    obj = get_object_or_404(Notification, id=pk)
    obj.viewed = True
    obj.save()

    data = {
      'viewed': True,
    }

    return Response(data)