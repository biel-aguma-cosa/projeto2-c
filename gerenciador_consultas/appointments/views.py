from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from appointments.models import Appointment
from appointments.forms  import AppointmentForm

# Create your views here.
@login_required
def view_appointment(request, id):
    context = dict()
    user = request.user

    context['appointment'] = Appointment.objects.get(id=id)

    if is_patient := hasattr(user, 'patient'):
            context['patient'] = user.patient       
    if is_professional := hasattr(user, 'professional'):
        context['professional'] = user.professional

    context['is_either'] = (is_patient or is_professional)

    if not context['is_either']:
        return redirect('admin:appointments_appointment_change', object_id=id)
    return render(request, 'professional_act.html', context)

@login_required
def list_view(request):
    if hasattr(request.user, 'patient'):
        patient = request.user.patient
        return render(request, 'list.html', {
            'patient':patient, 'appointments':patient.appointments.all})
    if hasattr(request.user, 'professional'):
        professional = request.user.professional
        return render(request, 'list.html', {
            'patient':professional, 'appointments':professional.appointments.all})
    if request.user.is_staff:
        return render(request, 'list.html', {'appointments':Appointment.objects.all()})
    return redirect('appointments:index')

def index(request):
    return HttpResponse('<h1>INDEX</h1>')
    