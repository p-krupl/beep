# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse,JsonResponse
from time import sleep
from django.utils import timezone
from django.db.models import F,Q
from django.core.urlresolvers import reverse



from .models import *
import json
from random import randint

# Create your views here.

@csrf_exempt
@require_http_methods(['GET', 'POST'])
def api(request,client_mac):
    if not request.method == 'POST':
      return HttpResponse('Hi there...., please post JSON')

    gameround = GameRound.objects.filter(ended=False).last()

    client_ip = request.META['REMOTE_ADDR']
    client,created = Client.objects.get_or_create(client_mac=client_mac)

    if not created:
        client.time_last_seen=timezone.now()
        client.save()
    
    json_data = json.loads(request.body)
    print "RX: %s" % client_ip
    print json_data

    if 'scan_data' in json_data and json_data['scan_data']:
        player_id = json_data['scan_data']
        print "GOT SCAN: %s !!!" % player_id

        player,player_created = Player.objects.get_or_create(player_id=player_id)

        if client.points_for_scan and gameround:
            Score.objects.create(
                player = player,
                client = client,
                points = client.points_for_scan,
                gameround = gameround,
                )
        
        client.points_for_scan = 0
        client.save()


    # Roll standard response

    response_dict = {}
    if client.dur_on != None:
        response_dict['dur_on'] = client.dur_on

    if client.dur_off != None:
        response_dict['dur_off'] = client.dur_off

    client.dur_on = None
    client.dur_off = None
    client.save()


    response_dict['auto_off'] = client.auto_off
    response_dict['post_interval'] = client.post_interval

    print "TX:"
    print response_dict
    return JsonResponse(response_dict)


class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name']
    template_name = 'player_form.html'
    
    def get_success_url(self):
        return reverse('player_list')

class PlayerList(ListView):
    model = Player
    template_name = 'player_list.html'

class GameRoundList(ListView):
    model = GameRound
    template_name = 'gameround_list.html'

    def get_queryset(self):
        return GameRound.objects.annotate(total_points=Sum('scores__points')).annotate(total_scores=Count('scores')).all()


class GameRoundDetail(DetailView):
    model = GameRound
    template_name = 'gameround_detail.html'


