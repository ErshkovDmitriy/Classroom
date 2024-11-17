from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    a = Post.objects.all()
    return render(request,'index.html', {'a': a})
