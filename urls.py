"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('clientes/', views.clientes, name='clientes'),
    path('locales/', views.locales, name='locales'),
    path('clientes/guardar', views.guardar, name='guardar'),
    path('locales/guardar', views.guardar, name='guardar'),
    path('clientes/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('locales/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('locales/detalle/<int:id>', views.detalle, name='detalle'),
    path('clientes/editar', views.editar, name='editar'),
    path('clientes/editar/<int:id>/', views.editar, name='editar')

]
