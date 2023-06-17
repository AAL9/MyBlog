from django import forms
from .models import Post

class PostBlog(forms.Form):
    title = forms.CharField(label="Title of the Blog", max_length=100)
    body = forms.CharField(label="Body of the Blog")

class PostComment(forms.Form):
    comment = forms.CharField(label="Comment")