import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'd3d6b5ad4cef4e7049c94628911aec59'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Barbie",
    "photo_id": 35
}

response_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_update = {
    "pokemon_id": pokemon_id,
    "name": "Ken",
    "photo_id": 29
}

response_update = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_update)
print(response_update.text)

body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

