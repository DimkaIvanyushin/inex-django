# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0005_breadcrumbssolution'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutions',
            name='short_description',
            field=models.CharField(default='default', max_length=250),
        ),
    ]