# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.template import RequestContext
from home.forms import LoginForm

# Create your views here.
def index_view(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def formulario_view(request):
	return render_to_response('registro/formulario.html', context_instance=RequestContext(request))

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
    	#si esta autenticado redirecciona al formulario
        return HttpResponseRedirect('/formulario')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/formulario')
                else:
                    mensaje = "Usuario y/o contraseña incorrecto"
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje}
        return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')