from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("post/<int:post_id>", views.post_page, name="post_page"),
    path("publish", views.publish, name="publish_page"),
]
