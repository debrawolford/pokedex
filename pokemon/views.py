from django.shortcuts import render
from django.http import HttpResponse

import json
import requests

offset = 0
limit = 20

while offset <= 140:
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/?limit={limit}&offset={offset}')
    response_json = response.json()
    for pokemon in response_json["results"]:
        name = pokemon["name"]
        url = pokemon["url"]
        res = requests.get(f'{url}')
        res_json = res.json()
        height = res_json["height"]
        _id = res_json["order"]
        sprite = res_json["sprites"]["front_default"]
        if len(res_json["abilities"]) == 0:
            print(name, height, _id, sprite)
        elif len(res_json["abilities"]) == 1:
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
        elif len(res_json["abilities"]) == 4:
            ability1 = res_json["abilities"][0]["ability"]["name"]
            ability2 = res_json["abilities"][1]["ability"]["name"]
            ability3 = res_json["abilities"][2]["ability"]["name"]
            ability4 = res_json["abilities"][2]["ability"]["name"]
            print(name, height, _id, sprite, ability1, ability2, ability4)
    if offset < 120:
        offset += 20
    else:
        limit = 11
        offset += 20

response_a = requests.get('https://pokeapi.co/api/v2/ability')
response_a_json = response_a.json()

for a in response_a_json["results"]:
    ability = a["name"]
    url = a["url"]
    res = requests.get(f'{url}')
    res_json = res.json()
    description = res_json["effect_entries"][1]["effect"]
    print(ability, description)





def home(request):
    template = 'pokemon/home.html'
    context = {
        'pokemon': response,
    }
    return render(request, template, context)
