from django.contrib import admin
from users.models import Patient, Professional, Qualification, ProfessionalQualification
# Register your models here.

def user__username(self):
    return self.user.username
def user__email(self):
    return self.user.email

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'phone', 'user__username', 'user__email']
    list_filter   = ['full_name',]
    search_fields = ['full_name', 'phone', 'user__username', 'user__email']

@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'phone', 'user__username', 'user__email']
    list_filter   = ['full_name',]
    search_fields = ['full_name', 'phone', 'user__username', 'user__email']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display  = ['name',]
    list_filter   = ['name',]
    search_fields = ['name',]

@admin.register(ProfessionalQualification)
class ProfessionalQualificationAdmin(admin.ModelAdmin):
    list_display  = ['professional','qualification']
    list_filter   = ['professional','qualification']
    search_fields = ['professional','qualification']
