# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_listing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bought',
            name='trans_id',
            field=models.CharField(blank=True, default='', max_length=8, null=True),
        ),
    ]