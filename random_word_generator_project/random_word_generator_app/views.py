from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

def index(request):
    return render(request,'index.html')

def random_word(request):
    request.session['counter'] += 1
    random_word = {
    'new_word' : get_random_string(length=14),
    'counter' : request.session.get('counter', 0)
    }
    return render(request, 'index.html', random_word)

def reset(request):
    request.session['counter'] = 0
    return render(request,'index.html')
