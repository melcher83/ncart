# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-09 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncart_app', '0003_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True, verbose_name='Email'),
        ),
    ]