from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "desc": 'The current time and date:'
    }
    return render(request,'index.html', context)
