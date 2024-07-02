from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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
