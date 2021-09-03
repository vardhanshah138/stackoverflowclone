from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length = 255)
    body = models.TextField()
    status = models.BooleanField(default=False)
    tags = TaggableManager()
    slug = models.SlugField(unique=True,max_length=100)

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

 

