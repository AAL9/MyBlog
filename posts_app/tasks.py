from time import sleep
from celery import shared_task
from blog.celery import app
from .models import Post
from django.utils import timezone


# @app.task
# def printing():
#     print("PRINTING PRINTING")


@app.task
def update_posts():
    current_datetime = timezone.now()

    scheduled_posts = Post.objects.filter(scheduled=True)

    for post in scheduled_posts:
        if post.publish_date < current_datetime:
            print("Updated post: ", post.id)
            post.scheduled = False
            post.save()
