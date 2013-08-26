#-*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django import http
from django.utils import timezone
from django.http import HttpResponse
from models import *
import json
import re



def events_json(request):
    # Get all events - Pas encore terminé
    events = Event.objects.all()

    # Create the fullcalendar json events list
    event_list = []

    for event in events:
        # On récupère les dates dans le bon fuseau horaire
        event_start = event.start.astimezone(timezone.get_default_timezone())
        event_end = event.end.astimezone(timezone.get_default_timezone())

        # On décide que si l'événement commence à minuit c'est un
        # événement sur la journée
        if event_start.hour == 0 and event_start.minute == 0:
            allDay = True
        else:
            allDay = False

        if not event.is_cancelled:
            event_list.append({
                    'id': event.id,
                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                    'end': event_end.strftime('%Y-%m-%d %H:%M:%S'),
                    'title': event.title,
                    'allDay': allDay
                    })

    if len(event_list) == 0:
        raise http.Http404
    else:
        return http.HttpResponse(json.dumps(event_list),
                                 content_type='application/json')

def Index(request):
    """
    @author Damien Goldenberg
    @name Index:
    @param - Request, HTTPRequest object
    @details Description:
    This is a view function. It displays the index
    """
    data = msg.objects.order_by('-id')[:12]
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
    if request.is_ajax() and request.POST.get("number") and request.POST.get("number") > 0:
        data = msg.objects.order_by('-id')[:12] if request.POST.get("number") == 1 else msg.objects.order_by('-id')[12*request.POST.get("number"):12*(request.POST.get("number")+1)]
        return render(request, 'blog.html', {'data':data})
    return render_to_response('42.html', {'data':'la page demandé n\'existe pas'})

def Article(request):
    if request.POST.get("id") and re.search("^a[0-9]{1,}$", request.POST.get("id")) and request.is_ajax():
        return render(request, 'article.html', {'data':msg.objects.filter(id=((request.POST.get("id")).split("a"))[1])})
    else:
        return render_to_response('42.html', {'data':'la page demandé n\'existe pas'})

def Control(request):
    if request.POST.get("id") and re.search("^[0-9]{1,}$", request.POST.get("id")) and request.is_ajax():
        id = int(request.POST.get("id"))
        views = ['blog', 'bda', 'poker', 'game', 'magic', 'music', 'theater', 'pfh', 'film', 'cook', 'draw', 'diary', 'rpg', 'picture', 'sponsor', 'contact', 'calendar', 'chauvin']
        if 0 <= id < len(views):
            data = msg.objects.order_by('-id')[:12] if id == 0 else ''
            return render_to_response(views[id]+'.html', {'data':data})
        else:
            return render_to_response('42.html', {'data':'la page demandé n\'existe pas'})
        return render_to_response('42.html', {'data':'42, The Big Question of Life, the Universe and Everything.'})
    else:
        return render_to_response('42.html', {'data':'hum hum ... are you stupid?'})