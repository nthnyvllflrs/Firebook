from django.db import models
from django.contrib.auth.models import User

from report.models import Report

RESPONDER_STATION = {
    ('Crime', 'Crime'),
    ('Fire', 'Fire'),
}

class Reporter(models.Model):
  user          = models.OneToOneField(User, on_delete=models.CASCADE)
  activated     = models.BooleanField(default=False)

  latitude      = models.CharField(max_length=30, blank=True, null=True)
  longitude     = models.CharField(max_length=30, blank=True, null=True)
  address       = models.TextField(max_length=300, blank=True, null=True)

  def __str__(self):
    return self.user.username


class Responder(models.Model):
  user          = models.OneToOneField(User, on_delete=models.CASCADE)
  
  phone_number  = models.CharField(max_length=30)
  station       = models.CharField(max_length=10, choices=RESPONDER_STATION)

  latitude      = models.CharField(max_length=30)
  longitude     = models.CharField(max_length=30)
  address       = models.TextField(max_length=300)

  def __str__(self):
    return self.user.username


