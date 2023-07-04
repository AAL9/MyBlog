from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Post


def update_posts():
    current_datetime = timezone.now()

    # Fetch posts with scheduled=True
    scheduled_posts = Post.objects.filter(scheduled=True)

    for post in scheduled_posts:
        if post.publish_date < current_datetime:
            post.scheduled = False
            post.save()
