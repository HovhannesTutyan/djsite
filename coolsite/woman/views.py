from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

menu=[{'title': 'About this site', 'url_name':'about'},
      {'title': 'Add an article', 'url_name':'add_page'},
      {'title':'Feedback', 'url_name':'contact'},
      {'title':'Enter','url_name':'login'}]


def index(request):
    posts=Woman.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title':'Main Page'
    }
    return render(request,'woman/index.html', context=context)
def about(request):
    return render(request,'woman/about.html', {'menu': menu, 'title':"About Page"})

def addpage(request):
    return HttpResponse("Add articles")
def contact(request):
    return HttpResponse("Contact us")
def login(request):
    return HttpResponse("Login")
def show_post(request, post_id):
    return HttpResponse(f"Showing posts with id = {post_id}")