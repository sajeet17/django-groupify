from django.db import models
from django.conf import settings

class Post(models.Model):
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	title= models.CharField(max_length=100,null=True, blank=True)
	status = models.TextField(max_length=500, null=True, blank=True)
	picture = models.ImageField(upload_to ='user_posts_pictures/',blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return '%s %s' %(self.user, self.timestamp)
