from django.shortcuts import render

from blog.models import Post


def show_blog(request):
    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts': posts})
