# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20171026_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='receipt_image',
            field=models.ImageField(upload_to='catalog/static/uploads/'),
        ),
    ]