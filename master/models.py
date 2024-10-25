from django.db import models
from django.urls import reverse

# Create your models here.
class NewsModel(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    images = models.ImageField(upload_to="upimages/")
    article = models.CharField(max_length=2000)
    timestamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']




class BlogModel(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    video = models.FileField(upload_to="upvideos/")
    timestamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

