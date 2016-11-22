# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from django.contrib import auth
from records.models import Book

@login_required
def main(request):
    args = {}

    if request.user.is_authenticated:
        user = auth.get_user(request)
        args['username'] = user
        args['records'] = Book.objects.filter(user=user.id)

        # records = Book.objects.filter(user=user.id)
        # paginator = Paginator(records, 30)
        #
        # try:
        #     args['records'] = paginator.page(page_number)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     args['records'] = paginator.page(1)
        # except InvalidPage:
        #     args['records'] = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     args['records'] = paginator.page(paginator.num_pages)

    return render_to_response('index.html', args)
