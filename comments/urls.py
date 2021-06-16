from comments.views import create
from django.urls import path

urlpatterns = [
    path('create/<str:post_pk>', create, name='comments-create'),
]
