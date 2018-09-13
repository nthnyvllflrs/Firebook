from django.contrib import admin

from .models import *

class ReportsAdmin(admin.ModelAdmin):
  list_display = ('reporter', 'emergency', 'timestamp')

admin.site.register(Report, ReportsAdmin)