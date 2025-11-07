from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import date
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


class Home(ListView):
    template_name = "blog/home.html"
    model = Post
    context_object_name = "allposts"
    #tutorial solution to ordering the query
    #ordering = ["-date"]
    def get_queryset(self):
        base_query = super().get_queryset()
        return base_query.order_by("-date")[:3]
        #return base_query[:3]

class Posts(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "allposts"
    ordering = ["-date"]
    
class Post(DetailView):
    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "p"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_post = self.object 
        context["tags"] = selected_post.tag.all()
        return context
"""  
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
"""