from django.shortcuts import render, redirect, reverse
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
