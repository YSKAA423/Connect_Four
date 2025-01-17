# Connect Four

This project serves as the first portfolio project in Codecademy's Computer Science Career path, targeting the introduction to programming section via Python.

## Project Goal

The goal of this project is to build a terminal-based, user-interactive game of **Connect Four**. It is designed as a two-player game, where players take turns dropping tokens into a grid, trying to connect four tokens in a row, column, or diagonal to win the game.

The game also supports a flexible grid size (e.g., 6x7 by default), where players can choose their own tokens and play against each other. This project can be extended further to include a CPU opponent.

### About Connect Four:
1. A 2-player game.
2. A dynamic, user-defined grid size (default suggested is 6 rows and 7 columns).
3. Players can choose their own token shapes.
4. The game checks for 4 connected tokens in any direction to declare a winner.
5. After a game ends, players can choose to restart or quit.

### Future Extensions:
- Add AI for CPU opponent.
- Implement a better user interface, such as graphical representation or web version.

## How to Play

1. Upon starting the game, players will be asked for their grid dimensions (rows and columns) and their chosen token shapes (e.g., 'X' and 'O').
2. Players take turns choosing a column to drop their token into.
3. The game automatically detects when a player has connected 4 tokens in a row, column, or diagonal, declaring the winner.
4. Players can restart the game or quit once the game concludes.

## Game Flow Example

### Example Output

```
---------------      Connect FOUR      ---------------
A 2 player game
A dynamic grid that is decided upon by the players
Each player gets to choose their own token
The program tracks the tokens and when 4 tokens connect in any direction then that player wins and that game concludes. (An Option to restart or to end to offered)
---------------      Connect FOUR      ---------------

Is the game on : 1 --> Yes , 0 --> No : 1
Enter the dimensions of the grid 'rows cols' -> e.g. '6 7': 6 7
Enter your token shape player 1: x
Enter your token shape player 2: d
-------Here is the base grid--------
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
-----------------------------------
Round 1
Player1: choose a column to drop into: [1, 2, 3, 4, 5, 6, 7] 1
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['x', 'O', 'O', 'O', 'O', 'O', 'O']
-----------------------------------
Player2: choose a column to drop into: [1, 2, 3, 4, 5, 6, 7] 2
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['x', 'd', 'O', 'O', 'O', 'O', 'O']
-----------------------------------
Round 2
Player1: choose a column to drop into: [1, 2, 3, 4, 5, 6, 7] 2
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'x', 'O', 'O', 'O', 'O', 'O']
['x', 'd', 'O', 'O', 'O', 'O', 'O']
-----------------------------------
Player2: choose a column to drop into: [1, 2, 3, 4, 5, 6, 7] 3
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', 'O', 'O']
['O', 'x', 'O', 'O', 'O', 'O', 'O']
['x', 'd', 'd', 'O', 'O', 'O', 'O']
-----------------------------------
Round 3
Player1: choose a column to drop into: [1, 2, 3, 4, 5, 6, 7] 4
...
```


