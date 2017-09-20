# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

## {u'post_interval': 5.0, u'scan_data': None, u'auto_off_fired': 0, u'dur_on': 0.8, u'auto_off': 1, u'dur_off': 0.4}

class Clients(models.Model):
    last_seen = models.DateTimeField(auto_now_add=True, db_index=True)
    client_mac = models.CharField(unique=True,max_length=12)
    name = models.CharField(unique=True,null=True,blank=True,max_length=255)
    auto_off = models.PositiveIntegerField(default=1)
    dur_on = models.FloatField(default=0.1)
    dur_off = models.FloatField(default=0.9)
    post_interval = models.FloatField(default=3)

    class Meta:
        pass


class Player(models.Model):
    player_id = models.CharField(max_length=16)
    name = models.CharField(unique=True,null=True,blank=True,max_length=255)
    last_seen = models.DateTimeField(auto_now_add=True, db_index=True)
