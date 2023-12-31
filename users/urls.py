from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("control/posts/", views.control_posts, name="control_posts"),
    path("control/posts/publish/", views.publish_post, name="publish_post"),
    path("control/posts/edit/<int:post_id>/", views.edit_post, name="edit_post"),
]
