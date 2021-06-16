from comments.models import Comment
from posts.models import Post
from django.shortcuts import redirect, render


def index(req):
    if req.user.is_authenticated:
        posts = Post.objects.order_by('-date_created').all()
        comments = Comment.objects.order_by('-date_created').all()

        context = {
            'posts': posts,
            'posts_filtered': posts[:3],
            'comments': comments
        }
        return render(req, 'pages/index.html', context)
    return redirect('login')
