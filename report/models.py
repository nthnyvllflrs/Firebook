from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Note : Do Migrations After Removing Comment
EMERGENCY_CHOICES = {
    # ('Crime', 'Crime'),
    ('Fire', 'Fire'),
}

REPOR_STATUS = {
    ('Ongoing', 'Ongoing'),
    ('Cleared', 'Cleared'),
}

class Report(models.Model):
  reporter    = models.ForeignKey(User, on_delete=models.CASCADE)
  responder   = models.ManyToManyField(User, related_name="is_responded", blank=True)
  verifies    = models.ManyToManyField(User, related_name="is_verified", blank=True)
  status      = models.CharField(max_length=10, choices=REPOR_STATUS, default="Ongoing")

  emergency   = models.CharField(max_length=10, choices=EMERGENCY_CHOICES)
  details     = models.CharField(max_length=300, blank=True)
  latitude    = models.CharField(max_length=50)
  longitude   = models.CharField(max_length=50)
  address     = models.TextField(max_length=300)

  image       = CloudinaryField('image')

  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return ("Emergency Report #" + str(self.id))


from cloudinary.models import CloudinaryField

class Photo(models.Model):
  image = CloudinaryField('image')