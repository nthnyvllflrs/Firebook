from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *
from .apis import *

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
    path('reporter/location/', reporter_location, name='reporter-location'),
    path('reporter/<slug:username>/', reporter_detail, name='reporter-detail'),

    path('responder/signup/', responder_signup, name='responder-signup'),
    path('responder/notifications/', responder_notifications, name='responder-notification'),
    path('responder/notifications/alerts/', responder_notifications_alerts, name='responder-notification-alert'),
    path('notification/<int:pk>/viewed/', NotificationViewedAPI.as_view(), name='responder-notification-viewed'),
    path('responder/<slug:username>/', responder_detail, name='responder-detail'),
]
