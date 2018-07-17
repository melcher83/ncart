# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Project(models.Model):
    client = models.CharField(verbose_name='Client', max_length=30)
    streetaddress = models.CharField(verbose_name='Street Address', max_length=300)
    city = models.CharField(verbose_name='City', max_length=30)
    state = models.CharField(verbose_name='State', max_length=30)
    zip = models.CharField(verbose_name='Zip Code', max_length=5)
    date = models.DateField(verbose_name='Date Performed')
    contact = models.CharField(verbose_name='Contact', max_length=100)

    def __unicode__(self):
        return self.Client
