from . import views
from django.urls import path

urlpatterns = [
    path("" , views.home, name = "home"),
    path("posts/" , views.posts , name = "posts"),
    path("posts/<slug:slug>/" , views.post , name = "post")
]