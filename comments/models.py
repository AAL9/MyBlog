from django.db import models
from posts.models import Post

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
