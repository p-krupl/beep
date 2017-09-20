# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from game.models import *
import operator

def frontpage(request):
    
    gameround = GameRound.objects.filter(ended=False).last()

    player_dict = {}
    for s in Score.objects.filter(gameround=gameround):
        if s.player in player_dict.keys():
            player_dict[s.player] += s.points
        else:
            player_dict[s.player] = s.points

    player_ranking_list = reversed(sorted(player_dict.items(), key=operator.itemgetter(1)))


    

    return render(request, 'frontpage.html', {
        'scores': Score.objects.all(),
        'player_ranking': player_ranking_list,
    })

