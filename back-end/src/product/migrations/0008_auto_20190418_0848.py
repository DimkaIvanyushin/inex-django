# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-18 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20190418_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specifications',
            name='icon',
            field=models.FileField(default='images/def/def.jpg', upload_to='images/product/icon'),
        ),
    ]
