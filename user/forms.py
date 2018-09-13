from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Reporter, Responder

RESPONDER_STATION = {
    ('Crime', 'Crime'),
    ('Fire', 'Fire'),
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
  

class ResponderForm(UserCreationForm):  

  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

  phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
  station = forms.ChoiceField(choices=RESPONDER_STATION, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Station'}))
  latitude = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}))
  longitude = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}))
  address = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 1, 'class': 'form-control', 'placeholder': 'Address'}))

  class Meta:
    model = User
    fields = (
      'username', 
      'email', 
    )


class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))