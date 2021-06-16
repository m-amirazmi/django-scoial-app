from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from posts.models import Post
from django.db.models.deletion import SET_NULL


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=SET_NULL)
    owner = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    text = models.TextField(blank=True)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.text
