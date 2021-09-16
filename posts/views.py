from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

def index(request):
    posts = Posts.objects.order_by('-published')
    return render(request, 'posts/index.html',{'posts': posts})
#    return HttpResponse("Hello World!!")
# http://127.0.0.1:8000/posts/

# Create your views here.
