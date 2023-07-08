from django import forms
from django.utils import timezone
from pytz import timezone as pytz_timezone


class PostBlog(forms.Form):
    title = forms.CharField(label="Title of the post", max_length=100)
    content = forms.CharField(label="Content of the post", widget=forms.Textarea())
    scheduled_date = forms.DateField(
        label="Publish at",
        widget=forms.SelectDateWidget(),
        initial=timezone.localdate(),
    )
    scheduled_time = forms.TimeField(
        label="", widget=forms.TimeInput(), initial=timezone.localtime().time()
    )


class EditPost(forms.Form):
    title = forms.CharField(
        label="Title of the post", max_length=100, initial="the title"
    )
    content = forms.CharField(
        label="Content of the post", widget=forms.Textarea(), initial="the content"
    )
    scheduled_date = forms.DateField(
        label="Publish at",
        widget=forms.SelectDateWidget(),
        initial=timezone.localdate(),
    )
    scheduled_time = forms.TimeField(
        label="", widget=forms.TimeInput(), initial=timezone.localtime().time()
    )


class PostComment(forms.Form):
    comment = forms.CharField(label="Comment")


class CommentDisplayed(forms.Form):
    def __init__(self, *args, **kwargs):
        comments = kwargs.pop("comments", [])  # Get the comments passed to the form
        super(CommentDisplayed, self).__init__(*args, **kwargs)

        for comment in comments:
            self.fields[f"comment_{comment.id}"] = forms.BooleanField(
                required=False,
                initial=comment.is_displayed,
                label=comment.comment,
            )
