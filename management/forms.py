# Django
from django import forms

# Local
from . import models as m

class CompanyForm(forms.ModelForm):
    
    class Meta:
        model = m.Company
        fields = '__all__'