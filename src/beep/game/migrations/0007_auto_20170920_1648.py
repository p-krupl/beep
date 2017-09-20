# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20170920_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='gameround',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='game.GameRound'),
        ),
    ]