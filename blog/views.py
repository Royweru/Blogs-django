from django.shortcuts import render, redirect
from .forms import BlogForm
from django.contrib.auth import login, logout, authenticate
from .models import User, Topic, Post
from django.contrib import messages


def home_page(request):
    posts = Post.objects.all()
    topics = Topic.objects.all()
    context = {'posts': posts, 'topics': topics}
    return render(request, 'base/Home.html', context)


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == 'POST':
        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'username does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'username and password do not exist')

        return redirect('home')

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def sign_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        messages.success(
            request, 'user  was created successfully!')
        login(request, user)
        return redirect('home')
    return render(request, 'base/signup.html')


def getblog(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'base/blogpage.html', context)


def createBlog(request):
    topics = Topic.objects.all()
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('home')

    context = {'topics': topics, 'form': form}
    return render(request, 'base/newpost.html', context)
