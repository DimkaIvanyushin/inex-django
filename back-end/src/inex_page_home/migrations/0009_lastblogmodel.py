# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-15 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('inex_page_home', '0008_alertmdlmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastBlogModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='inex_page_home_lastblogmodel', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='Latest Blog Posts', max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
