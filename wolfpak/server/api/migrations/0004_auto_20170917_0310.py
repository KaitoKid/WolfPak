# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-17 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170917_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need', models.IntegerField(choices=[(0, '911'), (1, 'FIRSTAID'), (2, 'EVACUATION'), (3, 'WATER'), (4, 'FOOD'), (5, 'PHONECHARGE'), (6, 'LIGHTS'), (7, 'MEDICATION'), (8, 'CLOTHING')])),
            ],
        ),
        migrations.RemoveField(
            model_name='quest',
            name='completed_on',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='owner',
        ),
        migrations.AddField(
            model_name='quest',
            name='distance',
            field=models.FloatField(default=0.8),
        ),
        migrations.AddField(
            model_name='quest',
            name='name',
            field=models.CharField(default='Kairui', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='status',
            field=models.IntegerField(choices=[(0, 'AVAILABLE'), (1, 'CLAIMED'), (2, 'COMPLETED')], default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quest',
            name='x_coord',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='quest',
            name='y_coord',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='wolf',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wolves', to='api.Family'),
        ),
        migrations.AddField(
            model_name='need',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needs', to='api.Quest'),
        ),
    ]
