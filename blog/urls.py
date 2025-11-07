from . import views
from django.urls import path

urlpatterns = [
    path("" , views.Home.as_view(), name = "home"),
    path("posts/" , views.Posts.as_view() , name = "posts"),
    path("posts/<slug:slug>/" , views.Post.as_view() , name = "post")
]