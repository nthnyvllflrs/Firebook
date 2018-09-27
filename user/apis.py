from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Notification

@api_view(['GET'])
def notification_viewed(request, pk):
  obj = get_object_or_404(Notification, id=pk)
  obj.viewed = True
  obj.save()

  data = {
    'viewed': True,
  }

  return Response(data)