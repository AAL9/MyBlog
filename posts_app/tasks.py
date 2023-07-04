from __future__ import absolute_import, unicode_literals
from time import sleep
from celery import shared_task





@shared_task
def scheduled_task():
    sleep(2)
    print("this is a scheduled task")