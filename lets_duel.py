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
print('Enter your pokemon (or leave blank and press enter for a random pokemon):')

# Get the user's choice
choice = input().lower()

# If the user presses enter without typing, assign a random Pokémon
if not choice.strip():
    choice = random.choice(pokemon_list)["name"]
    print(f"Random Pokémon assigned to you: {choice}")

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

# Our code starts here
# print(f"The number of pokemon is {len(pokemon_list)}")

# Function to get pokemon stats for battle
def get_pokemon_stats(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    # Getting and displaying the essential battle stats
    pokemon = {
        "name": data["name"],
        "hp": data["stats"][0]["base_stat"],       # HP
        "attack": data["stats"][1]["base_stat"],   # Attack
        "defense": data["stats"][2]["base_stat"]   # Defense
    }
    return pokemon

# Function to get a random Pokemon for CPU
def random_pokemon():
    rand_id = random.randint(1, 21)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{rand_id}/")
    data = response.json()
    return get_pokemon_stats(data["name"])


# Gets the player's Pokemon stats
player = get_pokemon_stats(choice)
# Gets the randomly picked Pokemon for CPU's stats
cpu = random_pokemon()
print("Your Pokemon:", player)
print("CPU's Pokemon:", cpu)


# This is the loop that creates the battle between the player & CPU
def battle(p1, p2):
    print(f"\nBattle starts! {p1['name'].title()} vs {p2['name'].title()}!\n")

# Loops keep running as long as player1 and player 2 (cpu) HP is greater than 0 (still alive)
    while p1["hp"] > 0 and p2["hp"] > 0:
        # This is where the player attacks the CPU
        damage = p1["attack"] - (p2["defense"] // 2) # // Rounds to nearest whole number (integer division)

        #Prevents zero or negative damage - damage will always be minimum '1'
        if damage < 1:
            damage = 1

        #subtracts the damage from oppenents hp
        p2["hp"] -= damage

        #prints attack results
        print(f"{p1['name'].title()} hits {p2['name'].title()} for {damage} damage!")
        print(f"{p2['name'].title()} HP left: {max(0, p2['hp'])}") # max functions ensures HP never prints as a negative number.

        # Checks if opponent has died
        if p2["hp"] <= 0:
            break

        # This is where the CPU attacks the player
        damage = p2["attack"] - (p1["defense"] // 2)
        if damage < 1:
            damage = 1

     #subtracts the damage from oppenents hp
        p1["hp"] -= damage

        #prints attack results
        print(f"{p2['name'].title()} hits {p1['name'].title()} for {damage} damage!")
        print(f"{p1['name'].title()} HP left: {max(0, p1['hp'])}") # max functions ensures HP never prints as a negative number.

#If condition to see which pokemon has won
    if p1["hp"] > 0:
        print(f"\nPokemon: {p1['name'].title()} wins the battle!")
    else:
        print(f"\nPokemon: {p2['name'].title()} wins the battle!")


# Runs the battle between player and CPU
battle(player, cpu)


