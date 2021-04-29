from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if not 'number' in request.session:
        request.session['count'] = 0
        random_number = random.randint(1, 100)
        request.session['number'] = random_number
    return render(request, 'index.html')

def test(request):
    chosen_number = int(request.session['number'])
    user_number = int(request.POST['number_guess'])
    request.session['user_guess'] = user_number
    if user_number == chosen_number:
        request.session['message'] = "You are correct!"
        context = {

        }
        return render(request, 'leaderboard.html', context)
    elif request.session['count'] == 4: 
        request.session['count'] += 1
        request.session['message'] = "You Lose!"
        return redirect('/')
    elif request.session['count'] == 5: 
        return reset(request)
    chosen_number = int(request.session['number'])
    user_number = int(request.POST['number_guess'])
    request.session['user_guess'] = user_number
    
    if user_number > chosen_number:
        request.session['message'] = "Too High!"
    else:
        request.session['message'] = "Too Low!"
    request.session['count'] += 1
    return redirect('/')

def reset(request):
    request.session['count'] = 0
    request.session['message'] = ""
    if 'number' in request.session:
        del request.session['number']
    if 'user_guess' in request.session:
        del request.session['user_guess']
    return redirect('/')
