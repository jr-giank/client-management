# Django
from django.db import models

# ----------------------------------------Address model----------------------------------------
class Addres(models.Model):
    
    street = models.CharField(verbose_name='Calle', max_length=150, blank=False, null=False)
    city = models.CharField(verbose_name='Ciudad', max_length=50, blank=False, null=False)
    state = models.CharField(verbose_name='Estado', max_length=50, blank=True, null=True)
    country = models.CharField(verbose_name='País', max_length=60, blank=False, null=False)
    
    def __str__(self):
        return f'{self.street} - {self.city} - {self.city}'
    
# ----------------------------------------Company model----------------------------------------
class Company(models.Model):
    
    company_name = models.CharField(verbose_name='Nombre de la Compañia', max_length=100, blank=False, null=False)
    address = models.ForeignKey(verbose_name='Dirección', to=Addres, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return f'{self.company_name}'