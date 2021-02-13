"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo),
    path('saludo2/', views.saludo2),
    path('nosvemos/', views.despedida),
    path('fecha/', views.fecha),
    path('edades/<int:edad>/<int:year>', views.calcula_edad),
    path('herencia/', views.herencia_plantilla),
    path('herencia2/', views.herencia_plantilla2),
]
