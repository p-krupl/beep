# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='dur_off',
            field=models.FloatField(default=0.2, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='dur_on',
            field=models.FloatField(default=0.2, null=True),
        ),
    ]
