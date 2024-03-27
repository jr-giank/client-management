# Django
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# Local
from . import models as m

User = get_user_model()

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number'
        ]
        
        help_texts = {
            'username': None,
        }

        labels = {
            'username': 'Nombre de Usuario',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'last_name': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'username': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'email': forms.EmailInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'phone_number': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'})
        }
        
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if password:
            return make_password(password)
        else:
            raise forms.ValidationError("La contraseña es requerida")

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'phone_number',
        ]
        
        help_texts = {
            'username': None,
        }

        labels = {
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'last_name': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'username': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'email': forms.EmailInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'password': forms.PasswordInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'phone_number': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'})
        }
        
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if password:
            return make_password(password)
        else:
            raise forms.ValidationError("La contraseña es requerida")
 
class LoginForm(forms.Form):
    
    email = forms.EmailField(
        label=('Correo Electrónico'),
        widget=forms.TextInput(
            attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}    
        ),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.'
        })
    
    password = forms.CharField(
        label=('Contraseña'),
        widget=forms.PasswordInput(
            attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}    
        ),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.'
        })
    
    