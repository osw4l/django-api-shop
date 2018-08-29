#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect


# Create your views here.


def log_in(request):
    context = {'error': False}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                if user.is_staff or user.is_superuser:
                    return redirect('admin:index')
                else:
                    return redirect('main:inicio')
            else:
                context = {'msj': _('El usuario ha sido desactivado'), 'error': True}
        else:
            context = {'msj': _('usuario o contraseña incorrecta'), 'error': True}
    return render(request, 'login.html', context)


@login_required
def salir(request):
    logout(request)
    return redirect('entrar')
