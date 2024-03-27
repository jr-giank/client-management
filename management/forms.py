# Django
from django import forms

# Local
from . import models as m

class AddressForm(forms.ModelForm):
    
    class Meta:
        model = m.Addres
        fields = ['street', 'city', 'state', 'country']
        
        widgets = {
            'street': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'city': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'state': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
            'country': forms.TextInput(attrs={'class': 'block p-2.5 w-full text-base text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500'}),
        }