from django.shortcuts import render
from django.http import HttpResponse

import requests

pokemon = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=150')

def home(request):
    template = 'pokemon/home.html'
    context = {
        'pokemon': pokemon,
    }
    return render(request, template, context)
