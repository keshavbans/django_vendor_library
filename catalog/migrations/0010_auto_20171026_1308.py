# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20171026_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='receipt_image',
            field=models.ImageField(upload_to='static/uploads/'),
        ),
    ]
