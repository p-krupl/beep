# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse,JsonResponse
from time import sleep

from .models import Clients
import json
from random import randint

# Create your views here.

@csrf_exempt
@require_http_methods(['GET', 'POST'])
def api(request,client_mac):
    if not request.method == 'POST':
      return HttpResponse('Hi there...., please post JSON')

    client,created = Clients.objects.get_or_create(client_mac=client_mac)
    
    json_data = json.loads(request.body)
    print "RX:"
    print json_data

    if 'scan_data' in json_data and json_data['scan_data']:
        print "GOT SCAN !!!"

    # Roll standard response
    return JsonResponse({
        'auto_off': client.auto_off,
        'dur_on': client.dur_on,
        'dur_off': client.dur_off,
        'post_interval': client.post_interval,
    })


