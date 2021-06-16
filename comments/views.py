from django.contrib.auth.models import User
from comments.models import Comment
from posts.models import Post
from accounts.models import Person
from django.shortcuts import redirect, render


def create(req, post_pk):
    if req.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        person = User.objects.get(username=req.user)
        comment = Comment(owner=person, post=post, text=req.POST['comment'])
        comment.save()
        return redirect('index')

# def edit(req, comment_pk):
#     if req.method == 'POST':
#         comment = Comment.objects.filter(pk=comment_pk)
#         comment.text = req.POST['comment']
