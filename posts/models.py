from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish_datetime = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=False)
    is_scheduled = models.BooleanField(default=False)
