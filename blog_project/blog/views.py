from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.


def home(requset):
    context = {
        'posts': Post.objects.all()
    }
    return render(requset, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})