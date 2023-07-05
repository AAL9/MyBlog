import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
app = Celery("blog")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "check-scheduled-posts-every-5-seconds": {
        "task": "posts_app.tasks.update_posts",
        "schedule": 5,
    },
}
