from django.urls import path

from .views import *

urlpatterns = [
    path('create/', report_create, name='report-create'),
]
