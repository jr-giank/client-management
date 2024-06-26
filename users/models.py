# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# ----------------------------------------User model----------------------------------------
class CustomUser(AbstractUser):
   
    first_name = models.CharField(verbose_name='Nombre', max_length=150, blank=False, null=False)
    last_name = models.CharField(verbose_name='Apellido', max_length=150, blank=False, null=False)
    email = models.EmailField(verbose_name='Correo Electrónico', blank=False, null=False, unique=True)
    phone_number = models.CharField(verbose_name='Número telefónico', max_length=12, default='', blank=True, null=False)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name'
    ]
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"