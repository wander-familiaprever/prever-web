from django.shortcuts import render, redirect, resolve_url, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from preverweb.core.models import Usuarios


def user_logout(request):
    try:
        del request.session['usuario_logado']
        del request.session['usuario']
    except KeyError:
        pass

    return HttpResponseRedirect(reverse('core:user_login'))


def user_login(request):
    template = loader.get_template('core/login.html')
    template_home = loader.get_template('core/home.html')

    context = {
        'usuario': '',
        'usuario_logado': False,
        'mensagem': '',
    }

    if request.method == 'POST':
        nome_usuario = request.POST.get('usuario')
        senha_usuario = request.POST.get('password')

        usuario = Usuarios.objects.filter(
            nome=nome_usuario).filter(senha=senha_usuario)
        nome = [u.nome for u in usuario]

        if len(nome) == 0:
            context['mensagem'] = 'Usuário ou senha não encontrado'
            return HttpResponse(template.render(context, request))
        else:
            request.session['usuario_logado'] = True
            request.session['usuario'] = nome

            context['usuario_logado'] = True

            return HttpResponseRedirect(reverse('core:index'))
    else:
        if request.session.get('usuario_logado'):
            context['usuario_logado'] = True
            context['usuario'] = str(request.session['usuario'])
            return HttpResponseRedirect(reverse('core:index'))
            #render(request, 'core/home.html', context=context)

    # HttpResponse(template.render({}, request))
    return HttpResponse(template.render({}, request))


def index(request):
    template = loader.get_template('core/home.html')

    usuario_logado = ''
    nome_usuario = ''

    if request.session.get('usuario_logado'):
        usuario_logado = request.session['usuario_logado']

    if request.session.get('usuario'):
        nome_usuario = request.session['usuario']

        context = {
            'usuario': str(nome_usuario[0]),
            'usuario_logado': usuario_logado,
        }
    else:
        context = {
            'usuario': str(nome_usuario),
            'usuario_logado': usuario_logado,
        }

    if context['usuario'] == '':
        return HttpResponseRedirect(reverse('core:user_login'))

    return HttpResponse(template.render(context, request))


def usuarios(request):
    usuarios = Usuarios.objects.all()
    usuarios_nomes = '<br/>'.join([u.nome for u in usuarios])
    return HttpResponse(usuarios_nomes)
