import datetime
from django.http import HttpResponse
from django.shortcuts import render

from .tasks import scheduled_task
# Create your views here.

def index(request):
    scheduled_task.delay()
    #return HttpResponse("Hi there!")