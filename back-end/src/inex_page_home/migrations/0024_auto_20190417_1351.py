# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inex_page_home', '0023_footermodel_description_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertctamodel',
            name='text',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='alertmdlmodel',
            name='title',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
