# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    username = models.CharField(verbose_name='Username', max_length=15)
    firstname = models.CharField(verbose_name='First Name', max_length=15)
    lastname = models.CharField(verbose_name='Last Name', max_length=15)
    email = models.EmailField(verbose_name='Email',null=True, default=None)
    phone = models.CharField(verbose_name='Phone', max_length=120)
    access = models.CharField(verbose_name='Access Level', max_length=10)

    def __unicode__(self):
        return self.user_auth.username