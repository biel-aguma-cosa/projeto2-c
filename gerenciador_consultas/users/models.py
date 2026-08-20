from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PatientManager(models.Manager):
    def new(self, full_name, phone, email = None):
        full_name = full_name.upper()
        name      = full_name.split(' ')[0]

        phone = phone
        email = email

        user    = User.objects.create_user(name, email, phone)
        patient = self.create(
            name  = name ,
            full_name = full_name,

            phone = phone,

            user  = user,)
        return patient
    
class Patient(models.Model):
    name      = models.CharField(max_length=20, verbose_name='Nome')
    full_name = models.CharField(max_length=80, verbose_name='Nome Completo')

    phone     = models.CharField(max_length= 9, verbose_name='Telefone')

    user      = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')

    objects   = PatientManager()
    class Meta:
        verbose_name        = 'Paciente'
        verbose_name_plural = 'Pacientes'
    def __str__(self):
        return self.full_name




class Qualification(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name        = 'Qualificação'
        verbose_name_plural = 'Qualificações'
    def __str__(self):
        return self.name
class ProfessionalManager(models.Manager):
    def new(self, full_name, phone, qualifications):
        #prof
        full_name = full_name.upper()
        name      = full_name.split(' ')[ 0]
        last_name = full_name.split(' ')[-1]

        phone = phone

        #user
        _username = f'{name.lower()}.{last_name.lower()}'
        username = _username
        n = 1
        while User.objects.filter(username=username).exists():
            username = f'{_username}.{n}'
        email    = f'{username}@domain.name'
        password = f'{last_name.capitalize()}321'
        user = User.objects.create_user(
            username, email, password,
        )
        #prof
        professional = self.create(
            name      = name ,
            phone     = phone,
            full_name = full_name,
            user = user,
        )
        for qualification in qualifications:
            ProfessionalQualification.objects.create(
                professional  = professional ,
                qualification = qualification,
            )
        return professional
class Professional(models.Model):
    name      = models.CharField(max_length=20, verbose_name='Nome')
    full_name = models.CharField(max_length=80, verbose_name='Nome Completo')

    phone     = models.CharField(max_length= 9, verbose_name='Telefone')

    user           = models.OneToOneField(User,
        verbose_name='Usuário',
        related_name='professional',
        on_delete=models.CASCADE,
        )
    qualifications = models.ManyToManyField(Qualification,
        through='ProfessionalQualification',
        verbose_name='Qualificações',
        related_name='professional',
        )

    objects = ProfessionalManager()
    class Meta:
        verbose_name        = 'Profissional'
        verbose_name_plural = 'Profissionais'
    def __str__(self):
        return self.full_name
    
    def delete(self, *args, **kwargs):
        self.appointments.update(
            status='CANCELLED'
        )
        super().delete(*args, **kwargs)
    
class ProfessionalQualification(models.Model):
    professional  = models.ForeignKey(
        Professional , verbose_name='Profissional' , on_delete=models.CASCADE)
    qualification = models.ForeignKey(
        Qualification, verbose_name='Qualification', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Qualificações do Profissional'
        verbose_name_plural = 'Qualificações dos Profissionais'
    def __str__(self):
        return f'{self.professional}, {self.qualification}'