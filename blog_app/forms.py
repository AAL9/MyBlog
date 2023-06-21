from django import forms

from posts_app.models import Post


class PostBlog(forms.Form):
    title = forms.CharField(label="Title of the Blog", max_length=100)
    body = forms.CharField(label="Body of the Blog", widget=forms.Textarea())


class PostComment(forms.Form):
    comment = forms.CharField(label="Comment")


class EditPost(forms.Form):
    title = forms.CharField(
        label="Title of the Blog", max_length=100, initial="the title"
    )
    body = forms.CharField(
        label="Body of the Blog", widget=forms.Textarea(), initial="the body"
    )
