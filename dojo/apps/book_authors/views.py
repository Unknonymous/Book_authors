# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

#views detailed below
def index(request):
    response ='Hello, I am the index seed for book_authors.'
    return HttpResponse(response)