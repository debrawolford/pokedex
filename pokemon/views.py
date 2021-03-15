from django.shortcuts import render
from django.http import HttpResponse

import json
import requests

offset = 0
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit=20')
response_json = response.json()

for pokemon in response_json["results"]:
    name = pokemon["name"]
    url = pokemon["url"]
    res = requests.get(f'{url}')
    res_json = res.json()
    height = res_json["height"]
    _id = res_json["order"]
    sprite = res_json["sprites"]["front_default"]
    if len(res_json["abilities"]) == 1:
        ability1 = res_json["abilities"][0]["ability"]["name"]
        print(name, height, _id, sprite, ability1)
    elif len(res_json["abilities"]) == 2:
        ability1 = res_json["abilities"][0]["ability"]["name"]
        ability2 = res_json["abilities"][1]["ability"]["name"]
        print(name, height, _id, sprite, ability1, ability2)
    elif len(res_json["abilities"]) == 3:
        ability1 = res_json["abilities"][0]["ability"]["name"]
        ability2 = res_json["abilities"][1]["ability"]["name"]
        ability3 = res_json["abilities"][2]["ability"]["name"]
        print(name, height, _id, sprite, ability1, ability2, ability3)


def home(request):
    template = 'pokemon/home.html'
    context = {
        'pokemon': response,
    }
    return render(request, template, context)
