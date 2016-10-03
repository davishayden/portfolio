from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
		name = models.CharField(max_length=200)
		type = models.CharField(max_length=500)
		created_At = models.DateTimeField('created at')
		pic_url = models.CharField(max_length=1000)