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
            'password',
            'photo',
            'phone_number'
        ]
        
        help_texts = {
            'username': None,
        }

        labels = {
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
        }

        widgets = {
            'password': forms.PasswordInput()
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
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.'
        })
    
    password = forms.CharField(
        label=('Contraseña'),
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.'
        })
    