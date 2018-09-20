from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Notification

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