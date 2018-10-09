from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

from report.models import Report

RESPONDER_STATION = {
    # ('Crime', 'Crime'),
    ('Fire', 'Fire Station'),
}

class Reporter(models.Model):
  user          = models.OneToOneField(User, on_delete=models.CASCADE)
  activated     = models.BooleanField(default=False)

  latitude      = models.CharField(max_length=30, blank=True, null=True)
  longitude     = models.CharField(max_length=30, blank=True, null=True)
  address       = models.TextField(max_length=300, blank=True, null=True)

  updated       = models.DateTimeField(auto_now_add=False, auto_now=True)
  timestamp     = models.DateTimeField(auto_now_add=True, auto_now=False)

  def __str__(self):
    return self.user.username


class Responder(models.Model):
  user          = models.OneToOneField(User, on_delete=models.CASCADE)
  display_name  = models.CharField(max_length=100)
  
  phone_number  = models.CharField(max_length=30)
  station       = models.CharField(max_length=10, choices=RESPONDER_STATION)

  latitude      = models.CharField(max_length=30)
  longitude     = models.CharField(max_length=30)
  address       = models.TextField(max_length=300)

  updated       = models.DateTimeField(auto_now_add=False, auto_now=True)
  timestamp     = models.DateTimeField(auto_now_add=True, auto_now=False)


  def __str__(self):
    return self.user.username


class Notification(models.Model):
  sender        = models.ForeignKey(User, on_delete=models.CASCADE)
  recipient     = models.ForeignKey(User, on_delete=models.CASCADE, related_name="is_recipient")

  report        = models.ForeignKey(Report, on_delete=models.CASCADE)
  title         = models.CharField(max_length=50)
  message       = models.CharField(max_length=300, blank=True, null=True)

  viewed        = models.BooleanField(default=False)

  updated       = models.DateTimeField(auto_now_add=False, auto_now=True)
  timestamp     = models.DateTimeField(auto_now_add=True, auto_now=False)

  def __str__(self):
    return ("Notification #" + str(self.id))