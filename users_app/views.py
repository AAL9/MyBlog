from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from blog_app.forms import PostBlog

from posts_app.models import Post


def register_user(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect(register_user)
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect(register_user)
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()

                return redirect("/")

        else:
            messages.info(request, "Both passwords are not matching")
            return redirect(register_user)

    else:
        return render(request, "users_app/register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect("/account/login")

    else:
        return render(request, "users_app/login.html")


def logout_user(request):
    auth.logout(request)
    return redirect("/")


def control_posts(request):
    if request.method == "POST":
        form = PostBlog(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            if request.POST.get("publish"):
                Post.objects.create(
                    post_owner_id=request.user.id,
                    title=title,
                    body=body,
                    last_update_date=timezone.now(),
                    publish_date=timezone.now(),
                )
            elif request.POST.get("save"):
                Post.objects.create(
                    post_owner_id=request.user.id,
                    title=title,
                    body=body,
                    last_update_date=timezone.now(),
                )
            return redirect("/")
    else:
        form = PostBlog()
    context = {"form": form,
               "user_posts":Post.objects.filter(post_owner_id=request.user.id)
               }
    return render(request, "users_app/control_posts.html", context)



def edit_post(request,post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post" : post,
    }
    return render(request,"users_app/edit_post.html",context)