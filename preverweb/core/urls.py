from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.index, name='index'),
    path('usuario/all', views.usuarios, name='usuarios'),
]
