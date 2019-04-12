# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='inex_page_home_aboutusmodel', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='Text', max_length=30)),
                ('description', models.TextField(default='Description')),
                ('img', models.ImageField(default='images/def/def.jpg', upload_to='images/about-us')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='MenuBarModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='inex_page_home_menubarmodel', serialize=False, to='cms.CMSPlugin')),
                ('phone_number', models.CharField(default='0-000-000-000', max_length=30)),
                ('phone_number_2', models.CharField(default='0-000-000-000', max_length=30)),
                ('locations', models.CharField(default='Улица Правды 30, Витебск 210029', max_length=30)),
                ('button_text', models.CharField(default='Заказать звонок', max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='inex_page_home_slideritem', serialize=False, to='cms.CMSPlugin')),
                ('text_bold', models.CharField(default='Text. Text.', max_length=30)),
                ('text', models.CharField(default='Text.', max_length=30)),
                ('img', models.ImageField(default='images/def/def.jpg', upload_to='images/slider')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SliderModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='inex_page_home_slidermodel', serialize=False, to='cms.CMSPlugin')),
                ('name_slider', models.CharField(default='Text.', max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
