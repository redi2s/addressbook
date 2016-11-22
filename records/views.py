# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.urls import reverse

from records.forms import BookForm
from records.models import Book

import django_excel as excel

@login_required
def add(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request)
    args['form'] = BookForm(request.user)

    if request.POST:
        form = BookForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            args['form'] = form

    return render_to_response('add.html', args)

@login_required
def edit(request, record):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request)

    # if record.isdigit():
    try:
        rec = Book.objects.get(id=record)
    except ObjectDoesNotExist:
        raise Http404

    args['form'] = BookForm(request.user, instance=rec)

    if request.POST:
        form = BookForm(request.user, request.POST, instance=rec)
        if form.is_valid():
            form.save()
            # return redirect(request.META.get('HTTP_REFERER', '/'))
            return HttpResponseRedirect(reverse('review', args=[rec.id]))
            # return redirect('/')
        else:
            args['form'] = form

    return render_to_response('edit.html', args)

@login_required
def review(request, record):
    args = {}
    args['username'] = auth.get_user(request)

    # if record.isdigit():
    try:
        args['record'] = Book.objects.get(id=record)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('review.html', args)

@login_required
def remove(request, record):
    try:
        Book.objects.get(id=record).delete()
    except ObjectDoesNotExist:
        raise Http404
    # return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')

@login_required
def export_data(request):
    user = auth.get_user(request)
    query_sets = Book.objects.filter(user=user)
    column_names = ['fullname', 'birthdate', 'address', 'phone', 'email', 'comment']
    return excel.make_response_from_query_sets(query_sets, column_names, 'csv', file_name='adbook_' + user.username)

@login_required
def search(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request)
    args['title'] = 'Результаты поиска'

    if 'q' in request.GET and request.GET['q']:
        user = auth.get_user(request)
        query = request.GET['q']
        args['query'] = query
        # args['products'] = Product.objects.filter(name__icontains=product_name)
        # В SQLite регистронезависимость не работает, ниже костыль
        args['records'] = Book.objects.filter(user=user).filter(Q(fullname__contains=query.lower()) | Q(fullname__contains=query.upper()) | Q(fullname__contains=query.capitalize()))

        return render_to_response('search.html', args)
    else:
        return render_to_response('search.html', args)
