# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloth',
            name='celebrity',
        ),
        migrations.AddField(
            model_name='cloth',
            name='celebrity',
            field=models.ManyToManyField(to='clothes.Celebrity'),
        ),
    ]
