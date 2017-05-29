# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('description', models.CharField(max_length=800)),
                ('is_completed', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('lesson_schedule', models.CharField(max_length=800)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='lessons',
            field=models.ManyToManyField(to='education.Lesson'),
        ),
    ]
