from django import forms

from posts_app.models import Post
from django.utils import timezone


class PostBlog(forms.Form):
    title = forms.CharField(label="Title of the Blog", max_length=100)
    body = forms.CharField(label="Body of the Blog", widget=forms.Textarea())
    scheduled_date = forms.DateField(
        label="publish at", widget=forms.SelectDateWidget(), initial=timezone.now()
    )
    scheduled_time = forms.TimeField(
        label="", widget=forms.TimeInput(), initial=timezone.now()
    )


class PostComment(forms.Form):
    comment = forms.CharField(label="Comment")


class EditPost(forms.Form):
    title = forms.CharField(
        label="Title of the Blog", max_length=100, initial="the title"
    )
    body = forms.CharField(
        label="Body of the Blog", widget=forms.Textarea(), initial="the body"
    )
    scheduled_date = forms.DateField(
        label="publish at", widget=forms.SelectDateWidget(), initial=timezone.now()
    )
    scheduled_time = forms.TimeField(
        label="", widget=forms.TimeInput(), initial=timezone.now()
    )
