# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0003_auto_20170921_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='celebrity',
            field=models.ManyToManyField(blank=True, to='clothes.Celebrity'),
        ),
    ]
