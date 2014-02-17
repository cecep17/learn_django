from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=30)
	description = models.TextField(max_length=200)
	active = models.BooleanField()