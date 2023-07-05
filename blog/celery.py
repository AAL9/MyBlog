import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
app = Celery("blog", timezone="Asia/Riyadh")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "check-scheduled-posts-every-minute": {
        "task": "posts_app.tasks.update_posts",
        # "schedule": crontab(minute='*/1'),
        "schedule": 5,
    },
}
