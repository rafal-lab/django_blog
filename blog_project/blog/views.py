from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(requset):
    return HttpResponse('<h1>Blog home</h1>')

def about(request):
    return HttpResponse('<h1>blog about</h1>')