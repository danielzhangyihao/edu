# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170426_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='activation_key',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(null=True),
        ),
    ]
