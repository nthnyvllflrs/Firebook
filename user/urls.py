from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='user/user-login.html', 
            authentication_form=LoginForm
        ), 
        name='user-login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='user-logout'),
    path('change-password/', change_password, name='change-password'),

    path('reporter/signup/', reporter_signup, name='reporter-signup'),
    path('responder/signup/', responder_signup, name='responder-signup'),
]