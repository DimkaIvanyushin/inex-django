# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_auto_20190417_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutions',
            name='img',
            field=models.ImageField(default='images/def/def.jpg', upload_to='images/solutions'),
        ),
    ]