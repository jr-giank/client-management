# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

#Local
from management import models as m

# ----------------------------------------User model----------------------------------------
class CustomUser(AbstractUser):
   
    first_name = models.CharField(verbose_name='Nombre', max_length=150, blank=False, null=False)
    last_name = models.CharField(verbose_name='Apellido', max_length=150, blank=False, null=False)
    email = models.EmailField(verbose_name='Correo Electrónico', blank=False, null=False, unique=True)
    company = models.ManyToManyField(verbose_name='Compañia', to=m.Company, related_name='user_companies', max_length=100, blank=True)
    photo = models.ImageField(verbose_name='Foto de perfil', upload_to='users/', default='users/default_image.jpg', blank=False, null=False)
    phone_number = models.CharField(verbose_name='Número telefónico', max_length=12, default='', blank=True, null=False)
    address = models.ManyToManyField(verbose_name='Dirección', to=m.Addres, related_name='user_addresses', max_length=100, blank=True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'password',
        'first_name',
        'last_name'
    ]
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"