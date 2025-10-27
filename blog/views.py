from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from .models import Post

# Create your views here.

def home(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request , "blog\home.html" , {
    "allposts" : latest_posts
    })

def posts(request):
    post = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html" , {
        "allposts" :post
    })

def post(request , slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request , "blog/post_detail.html",{
        "p" : identified_post,
        "tags": identified_post.tag.all()
    })