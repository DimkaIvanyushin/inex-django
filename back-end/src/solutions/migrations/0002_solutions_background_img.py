# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutions',
            name='background_img',
            field=models.ImageField(blank=True, default='images/def/def.jpg', null=True, upload_to='images/product', verbose_name='Фон'),
        ),
    ]
