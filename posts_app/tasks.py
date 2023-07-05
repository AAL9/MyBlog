from time import sleep
from celery import shared_task
from blog.celery import app


@app.task
def printing():
    print("PRINTING PRINTING")
