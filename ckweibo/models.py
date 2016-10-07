from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AuthCode(models.Model):
    username = models.CharField(max_length=30)
    authcode = models.CharField(max_length=32)