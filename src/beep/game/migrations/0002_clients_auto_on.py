# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='auto_on',
            field=models.BooleanField(default=True),
        ),
    ]
