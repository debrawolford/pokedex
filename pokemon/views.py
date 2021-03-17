from django.shortcuts import render
from django.http import HttpResponse

import json
import requests

# offset = 0
# limit = 20
# results = []

# while offset <= 140:
#     response = requests.get(f'https://pokeapi.co/api/v2/pokemon/?limit={limit}&offset={offset}')
#     response_json = response.json()
#     for pokemon in response_json["results"]:
#         name = pokemon["name"]
#         url = pokemon["url"]
#         res = requests.get(f'{url}')
#         res_json = res.json()
#         height = res_json["height"]
#         _id = res_json["order"]
#         sprite = res_json["sprites"]["front_default"]
#         if len(res_json["abilities"]) == 0:
#             data = {
#                 'model': 'pokemon.Pokemon',
#                 'pk': _id,
#                 'fields': {
#                     'name': name,
#                     'height': height,
#                     'sprite': sprite
#                 }
#             }
#         elif len(res_json["abilities"]) == 1:
#             ability1 = res_json["abilities"][0]["ability"]["name"]
#             data = {
#                 'model': 'pokemon.Pokemon',
#                 'pk': _id,
#                 'fields': {
#                     'name': name,
#                     'height': height,
#                     'sprite': sprite,
#                     'ability1': ability1
#                 }
#             }
#         elif len(res_json["abilities"]) == 2:
#             ability1 = res_json["abilities"][0]["ability"]["name"]
#             ability2 = res_json["abilities"][1]["ability"]["name"]
#             data = {
#                 'model': 'pokemon.Pokemon',
#                 'pk': _id,
#                 'fields': {
#                     'name': name,
#                     'height': height,
#                     'sprite': sprite,
#                     'ability1': ability1,
#                     'ability2': ability2
#                 }
#             }
#         elif len(res_json["abilities"]) == 3:
#             ability1 = res_json["abilities"][0]["ability"]["name"]
#             ability2 = res_json["abilities"][1]["ability"]["name"]
#             ability3 = res_json["abilities"][2]["ability"]["name"]
#             data = {
#                 'model': 'pokemon.Pokemon',
#                 'pk': _id,
#                 'fields': {
#                     'name': name,
#                     'height': height,
#                     'sprite': sprite,
#                     'ability1': ability1,
#                     'ability2': ability2,
#                     'ability3': ability3
#                 }
#             }
#         elif len(res_json["abilities"]) == 4:
#             ability1 = res_json["abilities"][0]["ability"]["name"]
#             ability2 = res_json["abilities"][1]["ability"]["name"]
#             ability3 = res_json["abilities"][2]["ability"]["name"]
#             ability4 = res_json["abilities"][2]["ability"]["name"]
#             data = {
#                 'model': 'pokemon.Pokemon',
#                 'pk': _id,
#                 'fields': {
#                     'name': name,
#                     'height': height,
#                     'sprite': sprite,
#                     'ability1': ability1,
#                     'ability2': ability2,
#                     'ability3': ability3,
#                     'ability4': ability4
#                 }
#             }
#         results.append(data)
#     if offset < 120:
#         offset += 20
#     else:
#         limit = 11
#         offset += 20
#     if len(results) == 151:
#         with open('pokemon_json.json', 'w') as f:
#             json.dump(results, f, indent=2)

# response_a = requests.get('https://pokeapi.co/api/v2/ability')
# response_a_json = response_a.json()
# results_abilities = []

# for a in response_a_json['results']:
#     ability = a['name']
#     url = a['url']
#     res = requests.get(f'{url}')
#     res_json = res.json()
#     effect = res_json['effect_entries'][1]['effect']
#     data = {
#         'model': 'pokemon.Ability',
#         'pk': 1,
#         'fields': {
#             'name': ability,
#             'effect': effect
#             }
#         }
#     results_abilities.append(data)

# with open('abilities_json.json', 'w') as f:
#     json.dump(results_abilities, f, indent=2)
    

def home(request):
    template = 'pokemon/home.html'
    return render(request, template)
