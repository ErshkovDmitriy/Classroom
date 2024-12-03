from .models import Request

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a = Request.objects.all()
    return render(request, 'index.html', {a: a})
