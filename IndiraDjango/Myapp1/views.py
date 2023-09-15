from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    data = {"name":"First WebPage"}
    return render(request,'Myapp1/Home.html',context=data)

def help(request):
    return HttpResponse("<h1>This is the Help Page</h1>")

def contact(request):
    return  HttpResponse("<h1>This is a Contact page</h1>")

