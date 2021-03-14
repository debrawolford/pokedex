from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template = 'pokemon/home.html'
    return render(request, template)
