from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
from django.core.urlresolvers import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def get_short_body(self):
        if len(self.body)>100:
            return self.body[:100]+'......'
        return self.body

class BlogPostForm(forms.ModelForm):
    class Mate:
        models = BlogPost
        exclude = ('timestamp',)

class BlogUser(models.Model):
    username = models.CharField(max_length= 20)
    def __unicode__(self):
        return self.username
class PrivateBlog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    username = models.ForeignKey(BlogUser,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.title