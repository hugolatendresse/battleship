# Battleship Game Simulator

This repository contains a Python-based Battleship game simulator. The simulator is designed to play a game of Battleship between two players. Each player can be AI, rule-based, or human.

## How to Run the Simulator

Run the simulator using the following command:

```sh
python main.py
```

## Game Rules
The game follows the standard rules of Battleship. Each player has a 10x10 board on which they place a number of boats. The players then take turns shooting at the opponent's board. If a shot hits a boat, the player gets another turn. The game continues until one player has sunk all of the opponent's boats.

In the game state, different numbers are used to represent different states:

0: water
1-4: a boat part that wasn't hit
10: a boat part that was hit but not sunk
15: a sunk boat


## Repository Structure

Here's a brief overview of the key files in this repository:

- [Player.py](Player.py): This file defines a Player class that represents a player in the game. Each player has their own board and a screen to track shots at the opponent. The player class also includes methods for choosing where to shoot next and for handling the situation when a boat is hit.
- [game.py](game.py): This file defines a Game class that represents a game of Battleship. It includes methods for updating the game state after each shot, checking if a boat is sunk, and sinking a boat.
- [field.py](field.py): This file defines a Field class that represents a game board. It uses the NewBoatField class from [boat_field.py](boat_field.py) to add boats to the field.
- [boat_field.py](boat_field.py): This file defines a NewBoatField class that is used to create a field with boats.
- [main.py](main.py): This is the main entry point for the simulator. It sets up the game and the players, and then runs the game.