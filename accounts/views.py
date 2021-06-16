from comments.models import Comment
from posts.models import Post
from accounts.models import Person
from accounts.forms import PersonForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from datetime import date


def register(req):
    if req.method == 'POST':
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        username = req.POST['username']
        password = req.POST['password']
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        person = Person(owner=user)
        person.save()

        return redirect('login')
    return render(req, 'accounts/register.html')


def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('index')
    return render(req, 'accounts/login.html')


def logout(req):
    auth.logout(req)
    return redirect('login')


def showProfile(req):
    form = PersonForm(instance=Person)
    person = Person.objects.get(owner=req.user)
    posts = Post.objects.order_by('-date_created').filter(owner=req.user)
    comments = Comment.objects.order_by('-date_created').all()
    posts_count = posts.count()

    context = {
        'date_joined': req.user.date_joined.date(),
        'form': form,
        'person': person,
        'posts': posts,
        'posts_count': posts_count,
        'posts_filtered': posts[:3],
        'comments': comments
    }
    return render(req, 'accounts/profile.html', context)


def editProfile(req):
    if req.method == 'POST':

        phone = req.POST['phone']
        bio = req.POST['bio']
        gender = req.POST['gender']
        print(gender)

        person = Person(owner=req.user, phone=phone, bio=bio, gender=gender)
        person.save()
        person = get_object_or_404(Person, owner=req.user)
        form = PersonForm(req.POST, instance=person)
        if form.is_valid():
            print('yes validdd')
            form.save()

        return redirect('profile')
    return render(req, 'accounts/profile.html')


def showOtherProfile(req, user_pk):
    person = Person.objects.get(owner=user_pk)
    posts = Post.objects.order_by('-date_created').filter(owner=user_pk)
    comments = Comment.objects.order_by('-date_created').all()
    posts_count = posts.count()
    context = {
        'person': person,
        'date_joined': person.owner.date_joined.date(),
        'posts': posts,
        'posts_count': posts_count,
        'posts_filtered': posts[:3],
        'comments': comments
    }
    return render(req, 'accounts/profile-other.html', context)
