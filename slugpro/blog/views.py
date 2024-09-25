# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
