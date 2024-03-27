# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required

# Local
from . import forms as f
from . import models as m
from management import models as mg
from management import forms as mf

User = get_user_model()

# ----------------------------------------Register and Login----------------------------------------

def registerView(request):
    
    if request.method == 'POST':
        form = f.RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = f.RegisterForm()
        
    return render(request=request, template_name='users/register.html', context={'form': form})
    
def loginView(request):
    
    if request.method == 'POST':
        form = f.LoginForm(request.POST)
        
        if form.is_valid():
            
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            
            if user is not None:
                login(request, user)
                
                return redirect('client_list')
            else:
                messages.error(request, "Correo o contraseña no valido.")
    else:
        form = f.LoginForm()
        
    return render(request=request, template_name='users/login.html', context={'form': form})

# ----------------------------------------Clients Views----------------------------------------

@login_required
def client_list(request):
    
    records = User.objects.prefetch_related('addresses').all()
    records_name = User._meta.get_fields(include_hidden=True)
    
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    records_name = [field for field in records_name if field.name in fields]
    
    UserAddressFormSet = formset_factory(mf.AddressForm, extra=1)

    if request.method == 'POST':
        form = f.UserForm(request.POST, request.FILES)
        address_formset = UserAddressFormSet(request.POST, prefix='addresses')

        if form.is_valid() and address_formset.is_valid():
            user = form.save()
            
            for form in address_formset:
                if form.cleaned_data:
                    street = form.cleaned_data.get('street')
                    city = form.cleaned_data.get('city')
                    state = form.cleaned_data.get('state')
                    country = form.cleaned_data.get('country')
                    
                    mg.Addres.objects.create(user=user, street=street, city=city, state=state, country=country)
            
            return redirect('client_list') 
    else:
        form = f.UserForm()
        address_formset = UserAddressFormSet(prefix='addresses')

    return render(request=request, template_name='list.html', context={'form': form, 'address_formset': address_formset, 'records': records, 'records_name': records_name})

@login_required
def client_update(request, pk):
    record = User.objects.get(id=pk)
    UserAddressFormSet = formset_factory(mf.AddressForm, extra=1)
    
    if request.method == 'POST':
        form = f.UserForm(request.POST, instance=record)
        address_formset = UserAddressFormSet(request.POST, prefix='addresses')
        
        if form.is_valid() and address_formset.is_valid():
            form.save()
           
            for form in address_formset:
                if form.cleaned_data:
                    street = form.cleaned_data.get('street')
                    city = form.cleaned_data.get('city')
                    state = form.cleaned_data.get('state')
                    country = form.cleaned_data.get('country')
                    mg.Addres.objects.create(user=record, street=street, city=city, state=state, country=country)
            
            return redirect('client_list') 
    else:
        form = f.UserForm(instance=record)
        address_formset = UserAddressFormSet(prefix='addresses')
        
    return render(request=request, template_name='update.html', context={'form': form, 'address_formset': address_formset})

@login_required
def client_delete(request, pk):
    
    record = User.objects.get(id=pk)
    
    if request.method == 'POST':
    
        record.delete()

        return redirect('client_list')
    
    return render(request=request, template_name='delete.html')
