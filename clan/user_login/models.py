from django.db import models
from django.conf import settings

class UserInfo(models.Model):

	user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
	first_name= models.CharField(max_length=30, blank=True, null=True)
	last_name = models.CharField(max_length=30 , blank= True, null=True)
	age = models.IntegerField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null= True)
	created_date = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.first_name