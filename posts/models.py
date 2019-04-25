from django.db import models
from django.conf import settings 
# Create your models here.
class Post(models.Model):
    title = models.TextField()
    #1:N
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="likeposts",blank=True)    

    