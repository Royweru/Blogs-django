from django.shortcuts import render,redirect
from .forms import BlogForm
from .models import User,Topic,Post
from django.contrib import messages


def home_page(request):
    posts = Post.objects.all()
    topics = Topic.objects.all()
    context = {'posts':posts,'topics':topics}
    return render(request, 'base/Home.html', context)


def getblog(request,pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'base/blogpage.html',context)

def createBlog(request):
    topics = Topic.objects.all()
    form =BlogForm()
    if request.method == 'POST':
        Post.objects.create(
            author = request.user,
            title = request.POST['title'],
            topic = request.POST['topic'],
            body = request.POST['body']
        )
        return redirect('home')
    context = {'topics':topics, 'form':form}
    return render(request, 'base/newpost.html',context )