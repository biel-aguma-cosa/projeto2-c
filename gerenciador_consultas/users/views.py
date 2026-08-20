from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required

from users.forms  import PatientForm, ProfessionalForm, ProfessionalModelForm, LoginForm, PasswordForm
from users.models import Patient, Professional

# Create your views here.
@login_required()
def index_view(request):
    context = dict()
    user = request.user

    if is_patient := hasattr(user, 'patient'):
        context['patient'] = user.patient       
    elif is_professional := hasattr(user, 'professional'):
        context['professional'] = user.professional
    context['is_either'] = (is_patient or is_professional)

    if request.method == 'POST':
        form = PasswordForm(user, request.POST)

        if form.is_valid():
            form.save()
            return redirect('users:index')
    else:
        form = PasswordForm(user)

    context['form'] = form

    return render(request, 'index.html', context)

@login_required()
def prof_view(request, id=None):
    if request.user.is_superuser:
        if id:
            professional = get_object_or_404(Professional,id=id)
            if request.method == 'POST':
                form = ProfessionalModelForm(request.POST, instance=professional)
                if form.is_valid():
                    form.save()
                    return redirect('users:list')
            else:
                form = ProfessionalModelForm(instance=professional)
            return render(request, 'register_professional.html', {
                'form':form, 'title':'Editar', 'professional':professional })
        
        else:
            if request.method == 'POST':
                form = ProfessionalForm(request.POST)
                if form.is_valid():
                    professional = Professional.objects.new(
                        form.cleaned_data['full_name'     ],
                        form.cleaned_data['phone'         ],
                        form.cleaned_data['qualifications'],)
                    professional.save()
                    return redirect('users:list')
            else:
                form = ProfessionalForm()
            return render(request, 'register_professional.html', {'form':form, 'title':'Registrar'})
    else:
        return redirect('users:index')

@login_required()
def list_view(request):
    if request.user.is_staff:
        return render(request, 'professional_list.html', {'professionals':Professional.objects.all()})
    else:
        return redirect('users:index')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('users:index')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('users:index')
    if request.method == 'POST':
        form = PatientForm(data = request.POST)
        if form.is_valid():
            patient = Patient.objects.new(
                full_name = form.cleaned_data['full_name'],
                phone = form.cleaned_data['phone'],
                email = form.cleaned_data['email'],)
            patient.save()

            login(request, patient.user)
            return redirect('users:index')
    else:
        form = PatientForm(data = request.POST)
    return render(request,'register.html',{'form':form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('users:index')