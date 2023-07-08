from django.http import HttpResponse
from django.shortcuts import render
from comments.models import Comment
from home.forms import PostComment
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post


def display_post_page(request, post_id):
    form = PostComment(request.POST)
    post = Post.objects.get(id=post_id)
    if post.publish_datetime is not None:
        context = {
            "post": post,
            "author": User.objects.get(id=post.owner_id),
            "comments": Comment.objects.filter(post=post_id),
            "form": form,
        }

        if form.is_valid():
            comment = form.cleaned_data["comment"]
            Comment.objects.create(post_id=post.id, comment=comment)

            return HttpResponseRedirect("/post/" + str(post_id))

        return render(request, "posts/post_page.html", context)
    else:
        return HttpResponse("ERROR!!")
