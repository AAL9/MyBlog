from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from posts_app.models import Post
from comments_app.models import Comment
from .forms import PostBlog, PostComment
from django.contrib.auth.models import User, auth
from posts_app import views
# Create your views here.


def home(request):
    context = {"titles": Post.objects.filter(publish_date__isnull=False)}
    views.index(request)
    return render(request, "blog_app/home.html", context)


def post_page(request, post_id):
    form = PostComment(request.POST)
    post = Post.objects.get(id=post_id)
    if post.publish_date is not None:
        context = {
            "post": post,
            "author": User.objects.get(id=post.post_owner_id),
            "comments": Comment.objects.filter(post=post_id),
            "form": form,
        }

        if form.is_valid():
            comment = form.cleaned_data["comment"]
            Comment.objects.create(post_id=post.id, comment=comment)

            return HttpResponseRedirect("/post/" + str(post_id))

        return render(request, "blog_app/post_page.html", context)
    else:
        return HttpResponse("ERROR!!")
