from time import sleep
from celery import shared_task
from blog.celery import app
from .models import Post
from django.utils import timezone
from blog.settings import TIME_ZONE

timezone.activate(TIME_ZONE)


@app.task
def update_posts():
    current_datetime = timezone.now()
    print("This is executed at:", timezone.now())

    scheduled_posts = Post.objects.filter(is_scheduled=True)

    for post in scheduled_posts:
        if post.publish_datetime < current_datetime:
            print("Updated post: ", post.id)
            post.is_scheduled = False
            post.save()
