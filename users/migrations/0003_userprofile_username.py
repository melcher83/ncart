# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180709_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=1, max_length=15, verbose_name='Username'),
            preserve_default=False,
        ),
    ]
