from django.shortcuts import render, HttpResponse, redirect
from time import strftime
import random

def index(request):
    return render(request, 'index.html')

def result(request):
    user_name = request.POST['name']
    user_gender = request.POST['gender']
    user_location = request.POST['location']
    user_fav_language = request.POST['language']
    user_known_languages = request.POST.getlist('lang_list[]')
    context = {
        "name" : user_name,
        "gender" : user_gender,
        "location" : user_location,
        "favorite_language" : user_fav_language,
        "known_languages" : user_known_languages
    }
    return render(request, 'result.html', context)