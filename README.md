# 🐉 PokéBash

A simple command-line Pokémon Battle game powered by the free [PokéAPI](https://pokeapi.co/).  
You can **choose your own Pokémon** or let the game **assign you a random one**. The CPU will always get a **random Pokémon**, and then they’ll fight until there’s a winner! ⚔️

---

## 🎮 How to Play

1. **Run the game** in your terminal:
```
   python lets_duel.py
   ```
The game will show you a list of available Pokémon.

You will be asked:
```
Enter your pokemon:
```
Type the name of a Pokémon from the list
OR press Enter without typing anything to get a random Pokémon
The CPU is automatically assigned a random Pokémon.

The battle begins!

Your Pokémon and the CPU’s Pokémon take turns attacking each other.
Damage is calculated based on attack and defense stats.
Battle continues until one Pokémon’s HP drops to 0.
The winner is declared! 🏆

To run the game you may need to install the relevant package:
```
pip install requests
```

Possible Error: If you enter a name that is not on the list, the program will crash.


# How we made the game

1. Made a remote repository called 'PokeBash' and added contributors
1. Made an Agile Board on Trello and discussed user stories, acceptance criteria, DoR and DoD
2. Moved items from Product Backlog to Sprint Backlog based on prioritization
3. Split the work: Dennis worked on the Function to get pokemon stats for battle and Saif worked on the Function to get a random pokemon for the CPU
4. Used git pull and push commands to work collaboratively on different branches
5. Came together to merge branches and resolve conflicts
6. Finished the battle loop together in Python
7. Final push to the remote repository too present working code
8. Discussed future plans to implement code to account for instances where the user enters a name not present on the list to make the code more robust


