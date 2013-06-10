#-*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import *
import json

def Index(request):
    """
    @author Damien Goldenberg
    @name Index:
    @param - Request, HTTPRequest object
    @details Description:
    This is a view function. It displays the index
    """
    return render(request, 'index.html', {})

def Co(request):
    """
    @author Damien Goldenberg
    @name Co:
    @param - Request, HTTPRequest object
    @details Description:
    This is a view function. It displays the connection form
    """
    return render(request, 'co.html', {})

def Blog(request):
    data = msg.objects.filter(id)
    return render(request, 'blog.html', {'data':data})

def Article(request):
    return render(request, 'article.html', {})