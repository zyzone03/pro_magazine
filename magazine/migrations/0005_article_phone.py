# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 10:56
from __future__ import unicode_literals

from django.db import migrations
import magazine.models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_auto_20160210_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='phone',
            field=magazine.models.PhoneField(blank=True, max_length=20),
        ),
    ]
