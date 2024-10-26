import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1ed0aacedd74cf408d00d3548d2a463c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "anna72-09@mail.ru",
    "password": "Anna2250436.kharchenko"
}


body_confirmation = {
    "trainer_token": TOKEN
}


body_create = {
    "name": "LOLA",
    "photo_id": 1
}
 
body_change = {
    "pokemon_id": "115311",
    "name": "Kiti",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "115311"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)


response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)




response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

