from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainWindow(Request):
    return HttpResponse(r"<a href='http://127.0.0.1:8000/app1_home'> Link</a><br> <h1> hello,, </h1>")

