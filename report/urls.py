from django.urls import path

from .views import *
from .apis import *

app_name = 'report'

urlpatterns = [
    path('create/', report_create, name='report-create'),
    path('timeline/', report_timeline, name='report-timeline'),
    
    path('<int:pk>/', report_detail, name='report-details'),
    path('<int:pk>/verify/', report_verify_toggle, name='report-verify-toggle'),
]
