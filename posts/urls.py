from django.urls import path
from . import views

urlpatterns = [
    path("<int:post_id>", views.display_post_page, name="post_page"),
]
