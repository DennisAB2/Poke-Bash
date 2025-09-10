import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))

# Function to get pokemon stats for battle
def get_pokemon_stats(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    # extract essential battle stats
    pokemon = {
        "name": data["name"],
        "hp": data["stats"][0]["base_stat"],       # HP
        "attack": data["stats"][1]["base_stat"],   # Attack
        "defense": data["stats"][2]["base_stat"]   # Defense
    }
    return pokemon

