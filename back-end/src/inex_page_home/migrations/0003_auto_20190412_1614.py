# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inex_page_home', '0002_smallfeaturesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='smallfeaturesmodel',
            name='icon_code',
            field=models.CharField(default='far fa-user', max_length=30),
        ),
        migrations.AlterField(
            model_name='smallfeaturesmodel',
            name='description',
            field=models.TextField(default='Text.'),
        ),
    ]
