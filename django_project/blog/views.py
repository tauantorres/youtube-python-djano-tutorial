from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Post


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    context = {
        'posts': Post.objects.all(),
    }
    return render(
        request=request, 
        template_name='blog/home.html',
        context=context,
    )

def about(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, 
        template_name='blog/about.html',
        context={'title': 'About'},
    )
