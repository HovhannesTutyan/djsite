from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

menu=['About this site', 'Add an article', 'Feedback', 'Enter']


def index(request):
    posts=Woman.objects.all()
    return render(request,'woman/index.html', {'posts':posts,'menu': menu, "title":"Главная страница"})
def about(request):
    return render(request,'woman/about.html', {'menu': menu, 'title':"About Page"})
def categories(request, catslug):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1> Articles by categories </h1> <p> {catslug} </p>")
def archive(request, year):
    return HttpResponse(f"<h1> Articles by year </h1> <p> {year} </p>")