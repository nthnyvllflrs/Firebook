from django.contrib.auth.models import User
from django.db import models

EMERGENCY_CHOICES = {
    ('Crime', 'Crime'),
    ('Fire', 'Fire'),
}


class Report(models.Model):
  reporter = models.ForeignKey(User, on_delete=models.CASCADE)
  verifies = models.ManyToManyField(User, related_name="is_verified", blank=True)

  emergency = models.CharField(max_length=10, choices=EMERGENCY_CHOICES)
  latitude = models.CharField(max_length=50)
  longitude = models.CharField(max_length=50)
  address = models.TextField(max_length=300)

  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return ("Emergency Report #" + str(self.id))
