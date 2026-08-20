from django.db import models
from users.models import Patient, Professional
# Create your models here.

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING   = 'PENDING'   , 'Pendente'
        CONFIRMED = 'CONFIRMED' , 'Confirmada'
        CANCELLED = 'CANCELLED' , 'Cancelada'

    patient      = models.ForeignKey(
        Patient, on_delete=models.CASCADE,
        verbose_name='Paciente', related_name='appointments'
    )
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE,
        verbose_name='Profissional', related_name='appointments'
    )

    date = models.DateField(verbose_name='Data')
    time = models.TimeField(verbose_name='Hora')

    subject = models.CharField(max_length=40 , verbose_name='Assunto')
    details = models.TextField(max_length=300, verbose_name='Detalhes')

    status  = models.CharField(
        max_length=10,
        choices = Status,
        default = Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criada em')
    updated_at = models.DateTimeField(auto_now    =True, verbose_name='Atualizada em')

    class Meta:
        verbose_name        = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f'{self.patient.name} | {self.date} - {self.time} | {self.professional.name}'