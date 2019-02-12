from django.db import models
import datetime


class UserInfo(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    profile_pic = models.ImageField()


class Post(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    pub_date = models.DateTimeField()
    tags = models.TextField(null=True)
    likes = models.IntegerField(default=0)
