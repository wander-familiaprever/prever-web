from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('', views.index, name='index'),
    path('usuario/all',views.usuarios, name='usuarios'),
]
