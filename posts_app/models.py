from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
