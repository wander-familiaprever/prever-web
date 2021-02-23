from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from preverweb.core.models import Usuarios

def login(request):
    template = loader.get_template('core/login.html')
    print('templaye = {}'.format(template))
    context = {
        'nome':'',
        'senha':'',
    }

    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('core/home.html')
    context = {}
    
    return HttpResponse(template.render(context, request)) 
   

def usuarios(request):
    usuarios = Usuarios.objects.all()
    usuarios_nomes =  '<br/>'.join([u.nome for u in usuarios])      
    return HttpResponse(usuarios_nomes)    
