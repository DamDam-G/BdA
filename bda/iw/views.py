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
    data = msg.objects.order_by('-id')
    return render(request, 'index.html', {'data':data})

def Co(request):
    """
    @author Damien Goldenberg
    @name Co:
    @param - Request, HTTPRequest object
    @details Description:
    This is a view function. It displays the connection form
    """
    return render(request, 'co.html', {})

def Register(request):
    """!
@author Damien Goldenberg
@name Co:
@param - Request, HTTPRequest object
@details Description:
This is a view function. It displays the connection form
"""
    return render(request, 'register.html', {})

def Blog(request):
    data = msg.objects.order_by('-id')
    return render(request, 'blog.html', {'data':data})

def Article(request):
    return render(request, 'article.html', {'data':msg.objects.filter(id=request.POST.get("id"))})

def Control(request):
    if request.POST.get("id") and request.is_ajax():
        id = int(request.POST.get("id"))
        views = ['blog', 'bda', 'int', 'game', 'magic', 'music', 'theater', 'pfh', 'film', 'cook', 'draw', 'diary', 'rpg', 'picture', 'sponsor', 'contact', 'calendrier']
        data = msg.objects.order_by('-id') if id == 0 else ''
        return render_to_response(views[id]+'.html', {'data':data})