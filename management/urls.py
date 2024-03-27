# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Local
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    
    path('company/list/', v.company_list, name='company_list'),
    path('company/create/', v.company_create, name='company_create'),
    path('company/update/<int:pk>/', v.company_update, name='company_update'),
    path('company/delete/<int:pk>/', v.company_delete, name='company_delete'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
