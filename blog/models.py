from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
from django.core.urlresolvers import reverse

class BlogUser(models.Model):
    username = models.CharField(max_length= 20)
    def __unicode__(self):
        return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def __unicode__(self):
        return self.title

class BlogPost2(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    tags = models.CharField(max_length=50,default='python')
    timestamp = models.DateTimeField()
    fuck = models.TextField()

    def __unicode__(self):
        return self.title

class PrivateBlog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    tag = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    username = models.ForeignKey(BlogUser,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.title