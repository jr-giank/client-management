# Django
from django.shortcuts import render, redirect

# Local
from . import models as m
from . import forms as f


# ----------------------------------------Company Views----------------------------------------
def company_list(request):
    
    records = m.Company.objects.all()
    records_name = m.Company._meta.fields
    
    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

def company_create(request):
    
    if request.method == 'POST':
        form = f.CompanyForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('company_list') 
    else:
        form = f.CompanyForm()
        
    return render(request=request, template_name='create.html', context={'form': form})

def company_update(request, pk):
    
    record = m.Company.objects.get(id=pk)
    
    if request.method == 'POST':
        form = f.CompanyForm(request.POST, instance=record)
        
        if form.is_valid():
            form.save()
            
            return redirect('company_list') 
    else:
        form = f.CompanyForm(instance=record)
        
    return render(request=request, template_name='update.html', context={'form': form})

def company_delete(request, pk):
    
    record = m.Company.objects.get(id=pk)
    
    if request.method == 'POST':
    
        record.delete()

        return redirect('company_list')
    
    return render(request=request, template_name='delete.html')

# ----------------------------------------Address Views----------------------------------------

        