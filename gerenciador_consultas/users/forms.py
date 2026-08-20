from django import forms
from users.models import Qualification, Professional
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from django.core.validators import RegexValidator

name_validator  = RegexValidator(
    regex=r'^[A-Za-zÀ-ÿ ]+$',
    message='Apenas letras e espaços são permitidos.'
)
phone_validator = RegexValidator(
    regex=r'^\d{9}$',
    message='Insira um número de telefone válido.'
)

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
class PasswordForm(PasswordChangeForm):
    old_password  = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
    }), label='Senha Anterior')
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
    }), label='Nova Senha')
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
    }), label='Nova Senha')


class PatientForm(forms.Form):
    full_name = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={
            'class':'form-control',
        }),
        label='Nome Completo',
        required=True,
        validators=[name_validator],
    )
    phone     = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={
            'class':'form-control',
        }),
        label='Telefone',
        required=True,
        validators=[phone_validator],
    )
    #optional
    email     = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-control',
        }),
        label='E-Mail',
        required=False,
    )

class ProfessionalForm(forms.Form):
    full_name = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={
            'class':'form-control',
        }),
        label='Nome Completo',
        required=True,
        validators=[name_validator],
    )
    qualifications = forms.ModelMultipleChoiceField(
        queryset=Qualification.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label='Qualificações',
        required=True,
    )
    phone = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={
            'class':'form-control',
        }),
        label='Telefone',
        required=True,
        validators=[phone_validator],
    )
class ProfessionalModelForm(forms.ModelForm):
    class Meta:
        model   = Professional
        fields  = ['name', 'full_name', 'qualifications']
        widgets = {
            'name'           : forms.TextInput(attrs={'class':'form-control',}),
            'full_name'      : forms.TextInput(attrs={'class':'form-control',}),

            'qualifications' : forms.CheckboxSelectMultiple(),
        }
