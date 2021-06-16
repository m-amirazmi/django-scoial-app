from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.post
