from django.db import models

class UserInfo(models.Model):
	username = models.CharField(max_length=30,blank=True,null=True)
	first_name= models.CharField(max_length=30, blank=True, null=True)
	last_name = models.CharField(max_length=30 , blank= True, null=True)
	age = models.IntegerField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	profile_picture = models.ImageField(upload_to='profile_picture/')

