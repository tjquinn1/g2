# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='zip',
            field=models.CharField(max_length=5),
        ),
    ]