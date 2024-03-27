# Django
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# ----------------------------------------Address model----------------------------------------
class Addres(models.Model):
    
    user = models.ForeignKey(verbose_name='Cliente', to=User, related_name='addresses', on_delete=models.CASCADE, max_length=100, blank=True)
    street = models.CharField(verbose_name='Calle', max_length=150, blank=False, null=False)
    city = models.CharField(verbose_name='Ciudad', max_length=50, blank=False, null=False)
    state = models.CharField(verbose_name='Estado', max_length=50, blank=True, null=True)
    country = models.CharField(verbose_name='País', max_length=60, blank=False, null=False)
    
    def __str__(self):
        return f'{self.user} - {self.city} - {self.state}'