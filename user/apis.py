from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Notification
from user.models import Reporter

@api_view(['GET'])
def notification_viewed(request, pk):
  obj = get_object_or_404(Notification, id=pk)
  obj.viewed = True
  obj.save()

  data = {
    'viewed': True,
  }

  return Response(data)


@api_view(['POST'])
def update_location(request):
  latitude = request.POST.get('latitude', None)
  longitude = request.POST.get('longitude', None)
  address = request.POST.get('address', None)

  user = User.objects.get(username=request.user)
  reporter = Reporter.objects.get(user=user)
  reporter.latitude = latitude
  reporter.longitude = longitude
  reporter.address = address
  reporter.save()

  data = {
    'updated': True,
  }

  return Response(data)