# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Project(models.Model):
    #Title = models.CharField(verbose_name='Title', max_length=30,null=True, default=None, blank=True)
    client = models.CharField(verbose_name='Client', max_length=30)
    streetaddress = models.CharField(verbose_name='Street Address', max_length=300)
    city = models.CharField(verbose_name='City', max_length=30)
    state = models.CharField(verbose_name='State', max_length=30)
    date = models.DateField(verbose_name='Date Performed')
    zip = models.CharField(verbose_name='Zip Code', max_length=5)
    date_end = models.DateField(verbose_name='Date Ended',null=True, default=None, blank=True)
    contact = models.CharField(verbose_name='Contact', max_length=100)
    email = models.EmailField(verbose_name='Email',null=True, default=None)

    def __unicode__(self):
        return self.client


class Firewall(models.Model):
    name = models.CharField(verbose_name='Firewall/Router/Switch Name', max_length=100)
    make = models.CharField(verbose_name='Brand',max_length=30)
    model = models.CharField(verbose_name='Model', max_length=30)
    description = models.CharField(verbose_name='Description', max_length=10000, null=True, default=None, blank=True)
    project = models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True)


    def __unicode__(self):
        return self.name

class Firewall(models.Model):
    name = models.CharField(verbose_name='Firewall/Router/Switch Name', max_length=100)
    make = models.CharField(verbose_name='Brand',max_length=30)
    model = models.CharField(verbose_name='Model', max_length=30)
    description = models.CharField(verbose_name='Description', max_length=10000, null=True, default=None, blank=True)



    def __unicode__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(verbose_class Firewall(models.Model):
    name = models.CharField(verbose_name='Firewall/Router/Switch Name', max_length=100)
    make = models.CharField(verbose_name='Brand',max_length=30)
    model = models.CharField(verbose_name='Model', max_length=30)
    description = models.CharField(verbose_name='Description', max_length=10000, null=True, default=None, blank=True)
    project = models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True)


    def __unicode__(self):
        return self.namename='Title', max_length=50)
    file = models.FileField()
    firewall = models.ForeignKey(Project, verbose_name="Firewall", null=True, default=None, blank=True)
    caption = models.ForeignKey(Project, verbose_name="Caption", null=True, default=None, blank=True)

    def __unicode__(self):
        return self.title

class Network_map(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    type = models.CharField(verbose_name='Type', max_length=20)
    file = models.FileField()
    project = models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True)
    caption = models.ForeignKey(Project, verbose_name="Caption", null=True, default=None, blank=True)

    def __unicode__(self):
        return self.title









