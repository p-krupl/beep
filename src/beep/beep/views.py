# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone


def frontpage(request):
    return render(request, 'frontpage.html')

