from django.contrib import admin

from appointments.models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display  = ['date', 'time', 'patient', 'professional', 'subject', 'created_at', 'updated_at', 'details']
    list_filter   = ['date', 'time']
    search_fields = ['patient', 'professional', 'subject', 'date', 'created_at']