# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0007_auto_20170921_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='visibility',
            field=models.BooleanField(default=False),
        ),
    ]