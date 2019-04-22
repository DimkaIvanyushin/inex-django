# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-22 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20190422_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupproduct',
            name='button_text_us',
        ),
        migrations.RemoveField(
            model_name='groupproduct',
            name='description_product',
        ),
        migrations.RemoveField(
            model_name='groupproduct',
            name='description_us',
        ),
        migrations.RemoveField(
            model_name='groupproduct',
            name='img_us',
        ),
        migrations.RemoveField(
            model_name='groupproduct',
            name='title_product',
        ),
        migrations.RemoveField(
            model_name='groupproduct',
            name='title_us',
        ),
        migrations.AddField(
            model_name='groupproduct',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='groupproduct',
            name='title_full',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Полное наименование'),
        ),
        migrations.AlterField(
            model_name='groupproduct',
            name='img',
            field=models.ImageField(blank=True, default='images/def/def.jpg', null=True, upload_to='images/product', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='groupproduct',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование'),
        ),
    ]