from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        character.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        character.extend(list('1234567890'))

    lenght = int(request.GET.get('lenght', 15))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html', {'password' : thepassword})
