from django.contrib import admin

from .models import *

class ReportsAdmin(admin.ModelAdmin):
  list_display = ('id', 'reporter', 'emergency', 'timestamp')

admin.site.register(Report, ReportsAdmin)


class NotificationsAdmin(admin.ModelAdmin):
  list_display = ('sender', 'recipient', 'title', 'report', 'timestamp')

admin.site.register(Notification, NotificationsAdmin)