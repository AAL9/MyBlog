from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from home.forms import PostBlog, EditPost
from datetime import datetime
from posts.models import Post
from django.contrib.auth.decorators import login_required


def register_user(request):
    if (not request.method == "POST") or None:
        return render(request, "users/register.html")
    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password != confirm_password:
            messages.info(request, "Both passwords are not matching")
            return redirect(register_user)
        else:  # this check is needed. If not provided, the page will crash
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


def login_user(request):
    if (not request.method == "POST") or None:
        return render(request, "users/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect("/account/login")


def logout_user(request):
    auth.logout(request)
    return redirect("/")


@login_required
def publish_post(request):
    if request.method == "POST":
        form = PostBlog(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            publish_datetime = datetime.combine(
                form.cleaned_data["scheduled_date"], form.cleaned_data["scheduled_time"]
            )
            publish_datetime_aware = timezone.make_aware(
                publish_datetime, timezone.get_current_timezone()
            )
            is_scheduled = False
            if publish_datetime_aware > timezone.now():
                is_scheduled = True
            else:
                publish_datetime = timezone.now()
                is_scheduled = False

            if request.POST.get("publish"):
                Post.objects.create(
                    owner_id=request.user.id,
                    title=title,
                    content=content,
                    last_updated_at=timezone.now(),
                    publish_datetime=publish_datetime,
                    is_scheduled=is_scheduled,
                )
            elif request.POST.get("save"):
                Post.objects.create(
                    owner_id=request.user.id,
                    title=title,
                    content=content,
                    last_updated_at=timezone.now(),
                    is_scheduled=is_scheduled,
                )
            return redirect("/")
    else:
        form = PostBlog()
    context = {
        "form": form,
    }
    return render(request, "users/publish_post.html", context)


@login_required
def control_posts(request):
    context = {
        "published_user_posts": Post.objects.filter(
            owner_id=request.user.id, publish_datetime__isnull=False
        ),
        "drafts": Post.objects.filter(
            owner_id=request.user.id, publish_datetime__isnull=True
        ),
    }
    return render(request, "users/control_posts.html", context)


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = EditPost(
        request.POST or None, initial={"title": post.title, "content": post.content}
    )
    context = {
        "post": post,
        "form": form,
    }
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        publish_datetime = datetime.combine(
            form.cleaned_data["scheduled_date"], form.cleaned_data["scheduled_time"]
        )
        publish_datetime_aware = timezone.make_aware(
            publish_datetime, timezone.get_current_timezone()
        )
        is_scheduled = False
        if publish_datetime_aware > timezone.now():
            is_scheduled = True
        else:
            publish_datetime = timezone.now()
            is_scheduled = False
        if request.POST.get("publish"):
            Post.objects.filter(id=post_id, owner_id=request.user.id).update(
                title=title,
                content=content,
                last_updated_at=timezone.now(),
                publish_datetime=publish_datetime,
                is_scheduled=is_scheduled,
            )
        elif request.POST.get("save"):
            Post.objects.filter(id=post_id, owner_id=request.user.id).update(
                title=title,
                content=content,
                last_updated_at=timezone.now(),
            )

        return redirect("/")
    return render(request, "users/edit_post.html", context)
