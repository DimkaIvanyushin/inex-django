# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 11:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inex_page_home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solutionsectionmodel',
            name='text',
        ),
    ]