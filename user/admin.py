from django.contrib import admin

from .models import *


class ReportersAdmin(admin.ModelAdmin):
  list_display = ('user', 'activated',)

admin.site.register(Reporter, ReportersAdmin)


class RespondersAdmin(admin.ModelAdmin):
  list_display = ('user', 'station', 'phone_number')

admin.site.register(Responder, RespondersAdmin)


class FightersAdmin(admin.ModelAdmin):
  list_display = ('name', 'responder', 'phone_number')

admin.site.register(Fighter, FightersAdmin)


class NotificationsAdmin(admin.ModelAdmin):
  list_display = ('sender', 'recipient', 'title', 'report', 'timestamp')

admin.site.register(Notification, NotificationsAdmin)