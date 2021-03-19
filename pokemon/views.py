from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Ability, Pokemon
from django.db.models import Q
from .forms import PokemonForm

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
    abilities = Ability.objects.all()
    context = {
        'pokemon': pokemon,
        'abilities': abilities
    }

    return render(request, template, context)

# View to display all abilities
def abilities(request):
    template = 'pokemon/abilities.html'
    abilities = Ability.objects.all()
    results_total_height = []
    results_total_pokemon = []
    for ability in abilities:
        total_height = 0
        total_pokemon = 0
        pokemon = Pokemon.objects.all()
        for pokemon in pokemon:
            if pokemon.ability1 == ability.name:
                total_pokemon += 1
                total_height += pokemon.height
            elif pokemon.ability2 == ability.name:
                total_pokemon += 1
                total_height += pokemon.height
            elif pokemon.ability3 == ability.name:
                total_pokemon += 1
                total_height += pokemon.height
            elif pokemon.ability4 == ability.name:
                total_pokemon += 1
                total_height += pokemon.height
        results_total_height.append(total_height)
        results_total_pokemon.append(total_pokemon)

    context = {
        'abilities': abilities,
        'pokemon': pokemon,
        'results_total_height': results_total_height,
        'results_total_pokemon': results_total_pokemon
    }
    return render(request, template, context)

# View to display Ability details
def ability_details(request, ability_id):
    template = 'pokemon/ability_details.html'
    ability = get_object_or_404(Ability, pk=ability_id)
    pokemon = Pokemon.objects.all()
    
    context = {
        'ability': ability,
        'pokemon': pokemon,
    }
    return render(request, template, context)

# View to create a new Pokemon
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            pokemon = form.save()
            return redirect(reverse('pokemon_details', args=[pokemon.id]))
        else:
            messages.error(request, ("Failed to add the new Pokemon,"))
    else:
        form = PokemonForm()

    template = 'pokemon/add_pokemon.html'
    context = {
        'form': form,
        'add_pokemon': True,
    }

    return render(request, template, context)