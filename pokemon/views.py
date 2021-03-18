from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Ability, Pokemon
from django.db.models import Q

import json
import requests


# View to display home page with all pokemon and images
def pokemon(request):
    template = 'pokemon/home.html'
    pokemon = Pokemon.objects.all().order_by('height')
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, ("Please enter what you are"
                                         " looking for."))
                return redirect(reverse('pokemon'))

            queries = (
                Q(name__icontains=query)
            )
            pokemon = pokemon.filter(queries)


    context = {
        'pokemon': pokemon,
        'search': query,
    }
    return render(request, template, context)

# View to display Pokemon details
def pokemon_details(request, pokemon_id):
    template = 'pokemon/pokemon_details.html'
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    context = {
        'pokemon': pokemon,
    }

    return render(request, template, context)

# View to display all abilities
def abilities(request):
    template = 'pokemon/abilities.html'
    abilities = Ability.objects.all()
    pokemon = Pokemon.objects.all()
    
    context = {
        'abilities': abilities,
        'pokemon': pokemon
    }
    return render(request, template, context)

# View to display Ability details
def ability_details(request, ability_id):
    template = 'pokemon/ability_details.html'
    ability = get_object_or_404(Ability, pk=ability_id)
    
    context = {
        'ability': ability,
    }
    return render(request, template, context)
