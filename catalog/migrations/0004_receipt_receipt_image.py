# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='receipt_image',
            field=models.ImageField(default='uploads/no-img.jpg', upload_to='uploads/'),
        ),
    ]
