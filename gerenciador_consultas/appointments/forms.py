from django import forms

from appointments.models import Appointment
from users.models import Patient, Professional

class AppointmentForm(forms.ModelForm):
    class Meta:
        model   = Appointment
        fields  = ['professional', 'patient', 'subject', 'details', 'date', 'time', 'status']
        widgets = {
            'professional' : forms.Select({'class':'form-control'}),
            'patient'      : forms.Select({'class':'form-control'}),
            'subject'      : forms.TextInput({'class':'form-control'}),
            'details'      : forms.Textarea ({'class':'form-control'}),
            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            ),
            'time'   : forms.TimeInput({'class':'form-control', 'type':'time'}),
            'status' : forms.Select({'class':'form-control'},choices=Appointment.Status)
        }