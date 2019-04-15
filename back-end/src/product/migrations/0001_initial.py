# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-15 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(default='images/def/def.jpg', upload_to='images/product')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('series', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.ImageField(default='images/def/def.jpg', upload_to='images/product')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.GroupProduct')),
            ],
        ),
    ]
