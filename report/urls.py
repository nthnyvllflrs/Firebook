from django.urls import path

from .views import *
from .apis import *

app_name = 'report'

urlpatterns = [
    path('create/', report_create, name='report-create'),
    path('timeline/', report_timeline, name='report-timeline'),
    path('cleared/', report_cleared, name='report-cleared'),
    
    path('<int:pk>/', report_detail, name='report-details'),
    path('<int:pk>/verify/', report_verify_toggle, name='report-verify-toggle'),
    path('<int:pk>/status/', report_status_toggle, name='report-status-toggle'),
    path('<int:pk>/respond/', report_respond, name='report-respond-toggle'),
]
