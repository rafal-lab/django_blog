from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'RafalFr',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 27, 2018'
    },
{
        'author': 'MichalFr',
        'title': 'Blog Post 2',
        'content': 'Second  Post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(requset):
    context = {
        'posts': posts
    }
    return render(requset, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})