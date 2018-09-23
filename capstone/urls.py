from django.contrib import admin
from django.urls import path, include

from .views import *

admin.site.site_header = 'Reportbook Administration'
admin.site.index_title = 'Reportbook'      
admin.site.site_title = 'Adminstrator'


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', landing, name='home'),
    path('responders/', responders, name='responders'),

    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('report/', include(('report.urls', 'report'), namespace='report')),
]
