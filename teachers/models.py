from django.db import models
from django.core.exceptions import ValidationError
import re

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    hire_date = models.DateField()
    subjects = models.ManyToManyField('Subject', related_name='teachers')

    def clean(self):
        # Verificação de número de telefone
        if self.phone_number and not re.match(r'^\+?1?\d{9,15}$', self.phone_number):
            raise ValidationError('Número de telefone inválido. Deve conter apenas dígitos.')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
