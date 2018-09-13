from django.contrib import admin

from .models import *

class ReportersAdmin(admin.ModelAdmin):
  list_display = ('user', 'activated',)

admin.site.register(Reporter, ReportersAdmin)

class RespondersAdmin(admin.ModelAdmin):
  list_display = ('user', 'station', 'phone_number')

admin.site.register(Responder)
