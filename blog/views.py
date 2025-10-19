from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request , "blog\home.html")

def posts(requests):
    pass

def post(request):
    pass