from django import forms

# Import all models inside report.models
from .models import *

# Constant
EMERGENCY_CHOICES = {
    # ('Crime', 'Crime'),
    ('Fire', 'Fire'),
}

class ReportForm(forms.ModelForm):
  emergency = forms.ChoiceField(choices=EMERGENCY_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Emergency'}))

  class Meta:
    model = Report
    fields = (
      'emergency', 'details', 'latitude', 'longitude', 'address',
    ) 

    widgets = {
      'details': forms.Textarea(attrs={'cols': 80, 'rows': 2, 'class': 'form-control', 'placeholder': 'Additional Information'}),
      'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
      'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
      'address': forms.Textarea(attrs={'cols': 80, 'rows': 2, 'class': 'form-control', 'placeholder': 'Address'}),
    }

  def clean_latitude(self):
    latitude = self.cleaned_data.get('latitude')
    try:
      tmp = float(latitude)
    except:
      raise forms.ValidationError("Invalid Latitude")
    return latitude
    
  def clean_longitude(self):
    longitude = self.cleaned_data.get('longitude')
    try:
      tmp = float(longitude)
    except:
      raise forms.ValidationError("Invalide Longitude")
    return longitude
