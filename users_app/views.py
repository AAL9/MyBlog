from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from home.forms import PostBlog, EditPost
from datetime import datetime
from posts.models import Post


def register_user(request):
    if (not request.method == "POST") or None:
        return render(request, "users_app/register.html")
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
        return render(request, "users_app/login.html")
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


def control_posts(request):
    if request.method == "POST":
        form = PostBlog(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            publish_date = datetime.combine(
                form.cleaned_data["scheduled_date"], form.cleaned_data["scheduled_time"]
            )
            publish_date_aware = timezone.make_aware(
                publish_date, timezone.get_current_timezone()
            )
            scheduled = False
            if publish_date_aware > timezone.now():
                scheduled = True
            else:
                publish_date = timezone.now()
                scheduled = False

            if request.POST.get("publish"):
                Post.objects.create(
                    post_owner_id=request.user.id,
                    title=title,
                    body=body,
                    last_update_date=timezone.now(),
                    publish_date=publish_date,
                    scheduled=scheduled,
                )
            elif request.POST.get("save"):
                Post.objects.create(
                    post_owner_id=request.user.id,
                    title=title,
                    body=body,
                    last_update_date=timezone.now(),
                    scheduled=scheduled,
                )
            return redirect("/")
    else:
        form = PostBlog()
    context = {
        "form": form,
        "published_user_posts": Post.objects.filter(
            post_owner_id=request.user.id, publish_date__isnull=False
        ),
        "drafts": Post.objects.filter(
            post_owner_id=request.user.id, publish_date__isnull=True
        ),
    }
    return render(request, "users_app/control_posts.html", context)


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = EditPost(
        request.POST or None, initial={"title": post.title, "body": post.body}
    )
    context = {
        "post": post,
        "form": form,
    }
    if form.is_valid():
        title = form.cleaned_data["title"]
        body = form.cleaned_data["body"]
        publish_date = datetime.combine(
            form.cleaned_data["scheduled_date"], form.cleaned_data["scheduled_time"]
        )
        publish_date_aware = timezone.make_aware(
            publish_date, timezone.get_current_timezone()
        )
        scheduled = False
        if publish_date_aware > timezone.now():
            scheduled = True
        else:
            publish_date = timezone.now()
            scheduled = False
        if request.POST.get("publish"):
            Post.objects.filter(id=post_id, post_owner_id=request.user.id).update(
                title=title,
                body=body,
                last_update_date=timezone.now(),
                publish_date=publish_date,
                scheduled=scheduled,
            )
        elif request.POST.get("save"):
            Post.objects.filter(id=post_id, post_owner_id=request.user.id).update(
                title=title,
                body=body,
                last_update_date=timezone.now(),
            )

        return redirect("/")
    return render(request, "users_app/edit_post.html", context)
