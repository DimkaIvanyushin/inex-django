# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-16 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_bg_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bg_color',
        ),
    ]
