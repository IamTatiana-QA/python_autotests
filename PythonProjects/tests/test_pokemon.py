import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'd3d6b5ad4cef4e7049c94628911aec59'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 4439

def test_status_code():
    response = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer():
    response_name = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()['data'][0]['trainer_name'] == 'Hamster'