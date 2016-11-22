# -*- coding: utf-8 -*-

from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf

from accounts.forms import UserCreateForm

def register(request):
    args = {}
    args.update(csrf(request))
    # args['form'] = UserCreationForm()
    args['form'] = UserCreateForm()
    if request.POST:
        # form = UserCreationForm(request.POST)
        form = UserCreateForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = form
    return render_to_response('register.html', args)
