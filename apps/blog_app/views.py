from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import PostBlog, PostComment

# Create your views here.


def Home(request):
    context = {"titles": Post.objects.all()}
    return render(request, "blog_app/home.html", context)


def PostPage(request, post_id):
    form = PostComment(request.POST)
    post = Post.objects.get(id=post_id)
    context = {
        "post": Post.objects.get(id=post_id),
        "comments": Comment.objects.filter(post=post_id),
        "form": form,
    }

    if form.is_valid():
        comment = form.cleaned_data["comment"]
        Comment.objects.create(post_id=post.id, comment=comment)

        return HttpResponseRedirect("/post/" + str(post_id))

    return render(request, "blog_app/post_page.html", context)


def Publsih(request):
    if request.method == "POST":
        form = PostBlog(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            print("THIS IS THE TITLE & BODY: ", title, body)
            Post.objects.create(title=title, body=body)
            return HttpResponseRedirect("/")
    else:
        form = PostBlog()
    context = {"form": form}
    return render(request, "blog_app/publish_page.html", context)
