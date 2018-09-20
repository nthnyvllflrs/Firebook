from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Report

@api_view(['GET'])
def report_verify_toggle(request, pk):
  obj = get_object_or_404(Report, id=pk)
  user = request.user

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