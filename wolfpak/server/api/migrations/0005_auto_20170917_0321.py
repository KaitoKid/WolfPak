# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-17 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170917_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='created_on',
            field=models.DateTimeField(blank=True),
        ),
    ]