from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import date
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.views import View
# Create your views here.


class HomeView(ListView):
    template_name = "blog/home.html"
    model = Post
    context_object_name = "allposts"
    #tutorial solution to ordering the query
    #ordering = ["-date"]
    def get_queryset(self):
        base_query = super().get_queryset()
        return base_query.order_by("-date")[:3]
        #return base_query[:3]

class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "allposts"
    ordering = ["-date"]
    
class PostView(View):
    def get(self, request , slug):
        selected_post = get_object_or_404(Post, slug= slug)
        context = {
            "p" : selected_post,
            "tags": selected_post.tag.all(),
            "comments" : selected_post.comments.all().order_by("-id"),
            "comment_form": CommentForm()
        }
        return render(request , "blog/post_detail.html", context)
    def post(self, request , slug):
        comment_form = CommentForm(request.POST)
        selected_post = get_object_or_404(Post, slug= slug)
        if comment_form.is_valid():
            commit_form = comment_form.save(commit=False)
            commit_form.post = selected_post
            comment_form.save()
            return HttpResponseRedirect(reverse_lazy("post" , args = [slug]))
        context = {
            "p" : selected_post,
            "tags": selected_post.tag.all(),
            "comments" : selected_post.comments.all().order_by("-id"),
            "comment_form": comment_form
        }
        return render(request , "blog/post_detail.html", context)


    
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