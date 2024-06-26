"""classswork URL Configuration

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
from django.urls import path, include
# from . import views
from django.views.generic import TemplateView #using this command means you don't have to create a views.py

urlpatterns = [
    # path('', views.index_page, name= 'Home'),
    path('', TemplateView.as_view(template_name = 'index.html'), name = 'Home'),

    # path('about/', views.about_page, name= 'About'),
     path('about/', TemplateView.as_view(template_name = 'about.html'), name = 'About'),

    # path('contact/', views.contact_page, name= 'Contact'),
     path('contact/', TemplateView.as_view(template_name = 'contact.html'), name = 'Contact'),

    # path('shop/', views.shop_page, name= 'Shop'),
     path('shop/', TemplateView.as_view(template_name = 'shop.html'), name = 'Shop'),

     path('',include('Adminapp.urls')),

    path('admin/', admin.site.urls),
]
