# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name='Username', max_length=15)
    firstname = models.CharField(verbose_name='First Name', max_length=15)
    lastname = models.CharField(verbose_name='Last Name', max_length=15)
    email = models.EmailField(verbose_name='Email',null=True, default=None)
    phone = models.CharField(verbose_name='Phone', max_length=120)
    access = models.CharField(verbose_name='Access Level', max_length=10)

    def __unicode__(self):
        return self.username