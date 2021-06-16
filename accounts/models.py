from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Person(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    phone = models.CharField(max_length=12, blank=True)
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=12, blank=True)
    image_cover = models.ImageField(upload_to='profile/cover/%Y/%m/%d/', blank=True)
    image_profile = models.ImageField(upload_to='profile/profile/%Y/%m/%d/', blank=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.owner.username
