from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_create(request):
    return HttpResponse('<h1>Create</h1>')

def post_detail(request):
    return HttpResponse('<h1>Detail</h1>')

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List'

    }
    return render(request, 'index.html', context)

def post_update(request):
    return HttpResponse('<h1>Update</h1>')

def post_delete(request):
    return HttpResponse('<h1>Delete</h1>')