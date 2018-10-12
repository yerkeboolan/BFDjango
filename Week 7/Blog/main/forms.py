from django.db import models
from django.forms import ModelForm
from .models import Posts, Comment


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = {'title', 'author', 'content', 'date_published'}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = {'email', 'created_date', 'comment_text'}