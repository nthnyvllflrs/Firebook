import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Reporter, Responder

RESPONDER_STATION = {
    # ('Crime', 'Crime'),
    ('Fire', 'Fire Station'),
}

class ReporterForm(UserCreationForm):

  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
  
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firstname'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lastname'}))

  class Meta:
    model = User
    fields = (
      'username', 
      'first_name', 
      'last_name', 
      'email',
    )

  def clean_email(self):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email__iexact=email)
    if qs.exists():
      raise forms.ValidationError("A user with that email already exists")
    return email
  

class ResponderForm(UserCreationForm):  

  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  display_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Display Name'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

  phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
  station = forms.ChoiceField(choices=RESPONDER_STATION, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Station'}))
  latitude = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}))
  longitude = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}))
  address = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 2, 'class': 'form-control', 'placeholder': 'Address'}))

  class Meta:
    model = User
    fields = (
      'username', 
      'email', 
    )

  def clean_email(self):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email__iexact=email)
    if qs.exists():
      raise forms.ValidationError("A user with that email already exists")
    return email

  def clean_phone_number(self):
    phone_number = self.cleaned_data.get('phone_number')
    if not re.match(r"(\+?\d{2}?\s?\d{3}\s?\d{3}\s?\d{4})|([0]\d{3}\s?\d{3}\s?\d{4})", phone_number):
      raise forms.ValidationError("Invalid Phone Number")
    return phone_number

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


class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
