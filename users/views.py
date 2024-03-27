# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Local
from . import forms as f

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