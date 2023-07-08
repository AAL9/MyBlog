from django.shortcuts import render
from posts.models import Post

# Create your views here.


def home(request):
    context = {
        "titles": Post.objects.filter(
            publish_datetime__isnull=False, is_scheduled=False
        )
    }
    return render(request, "home/home.html", context)
