# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20171024_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Name'),
        ),
    ]
