# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

# Local
from . import forms as f
from . import models as m
from management import models as mg

User = get_user_model()

# ----------------------------------------Register and Login----------------------------------------

def registerView(request):
    
    if request.method == 'POST':
        form = f.UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = f.UserForm()
        
    return render(request=request, template_name='users/register.html', context={'form': form})
    
def loginView(request):
    
    if request.method == 'POST':
        form = f.LoginForm(request.POST)
        
        if form.is_valid():
            
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            
            if user is not None:
                login(request, user)
                
                return redirect('register')
            else:
                messages.error(request, "Correo o contraseña no valido.")
    else:
        form = f.LoginForm()
        
    return render(request=request, template_name='users/login.html', context={'form': form})

# ----------------------------------------Clients Views----------------------------------------
def client_list(request):
    
    records = User.objects.all()
    records_name = User._meta.get_fields(include_hidden=True)
    
    fields = ['first_name', 'last_name', 'email', 'phone_number',]
    records_name = [field for field in records_name if field.name in fields]

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

def client_create(request):
    
    if request.method == 'POST':
        form = f.UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('client_list') 
    else:
        form = f.UserForm()
        
    return render(request=request, template_name='create.html', context={'form': form})

def client_update(request, pk):
    
    record = User.objects.get(id=pk)
    
    if request.method == 'POST':
        form = f.UserForm(request.POST, instance=record)
        
        if form.is_valid():
            form.save()
            
            return redirect('client_list') 
    else:
        form = f.UserForm(instance=record)
        
    return render(request=request, template_name='update.html', context={'form': form})

def client_delete(request, pk):
    
    record = User.objects.get(id=pk)
    
    if request.method == 'POST':
    
        record.delete()

        return redirect('client_list')
    
    return render(request=request, template_name='delete.html')
