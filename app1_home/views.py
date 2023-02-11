from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def welcome(Request):
    # return HttpResponse(" <h1 style='background:red'> welcome </h1> ")
    # my_dict = {'insert_me' : "I am Comming from views.py file of app1"}
    my_dict = {'insert_me': "I am Comming from subfolder app1_home/reg.html "}
    return render(Request    , r'app1\reg.html' ,context = my_dict)

