# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-22 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20190419_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupproduct',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]