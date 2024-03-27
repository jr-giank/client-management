# Django
from django.urls import path

# local
from . import views as v

urlpatterns = [
    path('register/', v.registerView, name='register'),
    path('login/', v.loginView, name='login'),
]
