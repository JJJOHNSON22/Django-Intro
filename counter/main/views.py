from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 0
    return render(request, 'index.html')

def reset(request):
    del request.session['count']
    return redirect('/')

def add_two(request):
    request.session['count'] += 1
    return redirect('/')
