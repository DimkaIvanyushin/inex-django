# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_groupproduct_background_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
    ]
