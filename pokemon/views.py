from django.shortcuts import render
from django.http import HttpResponse
from .models import Ability, Pokemon



# View to display home page with all pokemon
def home(request):
    template = 'pokemon/home.html'
    context = {
        'pokemon': Pokemon.objects.all(),
        'abilities': Ability.objects.all()
    }
    return render(request, template, context)
