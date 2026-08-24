from django.shortcuts import render, redirect, get_object_or_404
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
    context = dict()

    if request.user.is_staff:
        return render(request, 'list.html', {'appointments':Appointment.objects.all()})
    else:
        return redirect('appointments:my_list')

@login_required
def my_list_view(request):
    context = dict()

    if is_patient := hasattr(request.user, 'patient'):
        context['patient'] = request.user.patient
        context['is_patient'] = is_patient
        context['appointments'] = context['patient'].appointments.all
    if is_professional :=  hasattr(request.user, 'professional'):
        context['professional'] = request.user.professional
        context['is_professional'] = is_professional
        context['appointments'] = context['professional'].appointments.all
    
        return render(request, 'list.html', context)

@login_required
def edit_view(request, id):
    if request.user.is_staff:
        appointment = get_object_or_404(Appointment,id=id)
        if request.method == 'POST':
            form = AppointmentForm(request.POST, instance=appointment)
            if form.is_valid():
                form.save()
                return redirect('appointments:list')
        else:
            form = AppointmentForm(instance=appointment)

    return render(request,'edit.html',{'form':form, 'appointment':appointment,})

@login_required
def add_view(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = AppointmentForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('appointments:list')
        else:
            form = AppointmentForm()

    return render(request,'edit.html',{'form':form})

@login_required
def delete_view(request, id):
    if request.user.is_staff:
        appointment = get_object_or_404(Appointment,id=id)
        if appointment:
            appointment.delete()
    return redirect('appointments:list')

def index_view(request):
    return render(request, 'home.html', {})
    