from django.urls import path
from . import views
#from .models import Post

urlpatterns = [
    path('',views.Home,name="Home"),
    path('post/<int:post_id>',views.PostPage,name="post_page"),
    path('publish', views.Publsih, name = "publish_page")
]
