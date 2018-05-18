from django.db import models

class Post(models.Model):
	
	created_by = models.CharField(max_length=30)
	timestamp = models.DateTimeField(auto_now_add=True)
	