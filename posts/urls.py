from django.urls import path
from posts.views import create, delete, edit

urlpatterns = [
    path('create/', create, name='posts-create'),
    path('edit/<str:post_pk>/', edit, name='posts-edit'),
    path('delete/<str:post_pk>/', delete, name='posts-delete')
]
