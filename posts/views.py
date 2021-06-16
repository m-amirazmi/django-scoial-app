from posts.models import Post
from django.shortcuts import redirect, render
from datetime import datetime


def create(req):
    if req.method == 'POST':
        post = Post(owner=req.user, post=req.POST['post'])
        post.save()
        return redirect('index')
    return render('index')


def edit(req, post_pk):
    post = Post.objects.get(pk=post_pk)
    if req.method == 'POST':
        post.post = req.POST['post']
        post.date_created = datetime.now()
        post.save()
        return redirect('profile')

    context = {
        'post': post
    }
    return render(req, 'posts/edit.html', context)


def delete(req, post_pk):
    path = ''
    if 'profile' in req.META.get('HTTP_REFERER'):
        path = 'profile'
    else:
        path = 'index'
    post = Post.objects.filter(pk=post_pk)
    post.delete()
    return redirect(path)
