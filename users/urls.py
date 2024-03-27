# Django
from django.urls import path

# local
from . import views as v

urlpatterns = [
    path('register/', v.registerView, name='register'),
    path('login/', v.loginView, name='login'),
    
    path('', v.client_list, name='client_list'),
    path('client/update/<int:pk>/', v.client_update, name='client_update'),
    path('client/delete/<int:pk>/', v.client_delete, name='client_delete')
]
