from django import forms

from .models import *

EMERGENCY_CHOICES = {
    ('Crime', 'Crime'),
    ('Fire', 'Fire'),
}

class ReportForm(forms.ModelForm):

  emergency = forms.ChoiceField(choices=EMERGENCY_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Emergency'}))

  class Meta:
    model = Report
    fields = (
      'emergency', 'latitude', 'longitude', 'address',
    ) 

    widgets = {
      # 'emergency': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Emergency'}),
      'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
      'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
      'address': forms.Textarea(attrs={'cols': 80, 'rows': 2, 'class': 'form-control', 'placeholder': 'Address'}),
    }