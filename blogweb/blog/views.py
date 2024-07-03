from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('list_blogs')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

def list_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/list_blogs.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


@login_required
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.user != request.user:
        return redirect('list_blogs')
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/update_blog.html', {'form': form})

@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.user != request.user:
        return redirect('list_blogs')
    if request.method == 'POST':
        blog.delete()
        return redirect('list_blogs')
    return render(request, 'blog/delete_blog.html', {'blog': blog})



def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})