from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Ability, Pokemon



# View to display home page with all pokemon and images
def pokemon(request):
    template = 'pokemon/home.html'
    pokemon = Pokemon.objects.all().order_by('height')
    abilities = Ability.objects.all()
    query = None
    ability = None
    if request.GET:
        if 'ability' in request.GET:
            ability = request.GET['ability'].split()
            pokemon = pokemon.filter(ability__name__in=ability)
            ability = Ability.objects.filter(name__in=ability)

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
        'abilities': abilities,
        'search': query,
        'current_ability': ability
    }
    return render(request, template, context)

# View to display Pokemon details
def pokemon_details(request, pokemon_id):
    """ Renders product details on a specific product"""
    template = 'pokemon/pokemon_details.html'
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    context = {
        'pokemon': pokemon,
    }

    return render(request, template, context)
