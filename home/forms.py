from django import forms

from posts.models import Post
from django.utils import timezone


class PostBlog(forms.Form):
    title = forms.CharField(label="Title of the Blog", max_length=100)
    content = forms.CharField(label="content of the Blog", widget=forms.Textarea())
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
    content = forms.CharField(
        label="content of the Blog", widget=forms.Textarea(), initial="the content"
    )
    scheduled_date = forms.DateField(
        label="publish at", widget=forms.SelectDateWidget(), initial=timezone.now()
    )
    scheduled_time = forms.TimeField(
        label="", widget=forms.TimeInput(), initial=timezone.now()
    )
