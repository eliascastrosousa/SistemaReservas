'''
 1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
'''

from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('authtwofactor/', views.authtwofactor, name='authtwofactor'),
    path('perfil/', views.perfil, name='perfil')
    
]
