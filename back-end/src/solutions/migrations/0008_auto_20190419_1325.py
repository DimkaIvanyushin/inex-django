# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-19 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0007_auto_20190419_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solutionspluginmodel',
            name='description_us',
        ),
        migrations.RemoveField(
            model_name='solutionspluginmodel',
            name='text_button_us',
        ),
        migrations.RemoveField(
            model_name='solutionspluginmodel',
            name='title_us',
        ),
        migrations.AddField(
            model_name='solutions',
            name='description_us',
            field=models.TextField(default='default'),
        ),
        migrations.AddField(
            model_name='solutions',
            name='text_button_us',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='solutions',
            name='title_us',
            field=models.CharField(default='default', max_length=100),
        ),
    ]