# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.db.models import Count, Min, Sum, Avg

# Create your models here.

## {u'post_interval': 5.0, u'scan_data': None, u'auto_off_fired': 0, u'dur_on': 0.8, u'auto_off': 1, u'dur_off': 0.4}

class Client(models.Model):
    time_last_seen = models.DateTimeField(auto_now_add=True, db_index=True)
    client_mac = models.CharField(unique=True,max_length=12)
    name = models.CharField(unique=True,null=True,blank=True,max_length=255)

    # Theese fields below are the values sent to the Client.
    auto_off = models.PositiveIntegerField(default=1)
    dur_on = models.FloatField(null=True,default=0.2)
    dur_off = models.FloatField(null=True,default=0.2)
    post_interval = models.FloatField(default=3)

    # Theese fiels handle interal point giving.
    points_for_scan = models.IntegerField(default=0)

    class Meta:
        pass


class Player(models.Model):
    player_id = models.CharField(max_length=16,unique=True)
    name = models.CharField(unique=True,null=True,blank=True,max_length=255)
    time_last_seen = models.DateTimeField(auto_now_add=True, db_index=True)

    def score(self,gameround):
        point_list = self.scores_set.filter(gameround=gameround).values_list('points',flat=True)
        if point_list:
            return sum(point_list)
        else:
            return 0


class GameRound(models.Model):
    time_created = models.DateTimeField(auto_now_add=True, db_index=True)
    ended = models.BooleanField(default=False)
    points_goal = models.IntegerField(default=10)

    class Meta:
        ordering = ['time_created']



class Score(models.Model):
    time_created = models.DateTimeField(auto_now_add=True, db_index=True)
    player = models.ForeignKey('game.Player',db_index=True)
    gameround = models.ForeignKey('game.GameRound',db_index=True,related_name='scores')
    client = models.ForeignKey('game.Client') 
    points = models.IntegerField(default=0)


