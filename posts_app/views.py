import datetime
from django.shortcuts import render

# Create your views here.
from .tasks import my_scheduled_task
def register_task():
    # Schedule the task to run every day at 8:00 AM
    my_scheduled_task.schedule(repeat=Task.DAILY, time=datetime.time(hour=8, minute=0))
