# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_auto_20171120_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='bought',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
