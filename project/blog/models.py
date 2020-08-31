from django.db import models


class Signup(models.Model):
	username = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=20)
	
	def __str__(self):
		return self.username

class Newblog(models.Model):
	blogname = models.CharField(max_length=20)
	description = models.TextField()