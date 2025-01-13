"""
This project serves as the first portfolio project Codedacdemy's Computer Science Career path
targeting the introduction to programming section via Python.

The Goal of this project is to make a terminal based user-interactive project. I have choosen the famous
Connect Four as the backbone for this project as it can be a fun project to build upon as my skillset evolves.

The basic implementation involves:
    1 - A 2 player game. (A game against a CPU can be added later on)
    2 - A Grid of flexible sizes. (e.g. 6 by 7)
    3 - Each player gets to choose their own token.
    4 - The program tracks the tokens and when 4 tokens connect in any direction then
        that player wins and that game concludes. (An Option to restart or to end is offered)
    
I have seen some resources where AI plays against itself to train and then can be used to play against, this 
is a very interesting concept that can be touched upon. I understand that I am not inventing new tech but hopefully this project 
enforces solid and expansive programming principles. 
"""

Rules = {1:"A 2 player game", 
2:"A dynamic grid that is decided upon by the players",
3:"Each player gets to choose their own token",
4:"The program tracks the tokens and when 4 tokens connect in any direction then that player wins and that game concludes. (An Option to restart or to end to offered)"}

# Initializing the Grid
def grid_init(rows,drops):
    global initial_grid 
    initial_grid = [["O" for d in range(drops)] for r in range(rows)]
    return initial_grid

# Showing the Grid
def show_grid(recieved_grid):
    for row in recieved_grid:
        print(row)
    print("-----------------------------------")

# Checking if the column choosen within range
def column_check(column_to_drop, p, cols):
    while True:
        column_to_drop = int(input(f"Player {p}: choose a column to drop into: {[x+1 for x in range(cols)]} ")) - 1         
        if 0 <= column_to_drop < cols:
            return column_to_drop
        else:
            print(f"Invalid column. Please select a number between 1 and {cols}.")

# Finding the empty slots and filling them
def find_slot(grid,shape,rows, column_to_drop):
    for r in range(rows-1, -1, -1):
        if (r, column_to_drop) in Empty_slots:
            grid[r][column_to_drop] = shape
            Filled_slots.append((r,column_to_drop))
            Empty_slots.remove((r,column_to_drop))
            return grid
    print("No Slots left in that column")
    return grid

# Checking all filled slots in order to find if four shapes are connected
def check_filled_slots(filled_slots, dimensions: tuple):
    def check_player(slots_p):
        positions = set((r, c) for r, c in slots_p)

        # Check horizontal, vertical, and both diagonals
        for r, c in slots_p:
            # Horizontal: Check if there are 4 connected tokens horizontally
            if all((r, c + i) in positions for i in range(4)) and c + 3 < dimensions[1]:
                return 1

            # Vertical: Check if there are 4 connected tokens vertically
            if all((r + i, c) in positions for i in range(4)) and r + 3 < dimensions[0]:
                return 1

            # Diagonal (top-left to bottom-right): Check if there are 4 connected tokens diagonally
            if all((r + i, c + i) in positions for i in range(4)) and r + 3 < dimensions[0] and c + 3 < dimensions[1]:
                return 1

            # Diagonal (bottom-left to top-right): Check if there are 4 connected tokens diagonally
            if all((r - i, c + i) in positions for i in range(4)) and r - 3 >= 0 and c + 3 < dimensions[1]:
                return 1

    slots_p1 = filled_slots[::2]  # Flitering player one moves
    slots_p2 = filled_slots[1::2]  # # Flitering player two moves

    if check_player(slots_p1):
        print("Player 1 has won")
        return 1

    if check_player(slots_p2):
        print("Player 2 has won")
        return 1

    if len(filled_slots) == (dimensions[0] * dimensions[1]):
        print("It is a draw")
        return 1



print("---------------      Connect FOUR      ---------------")

for rules in Rules.values():
    print(rules)
    
print("---------------      Connect FOUR      ---------------")

game_on = bool(int(input("Is the game on : 1 --> Yes , 0 --> No : "))) 

while game_on:
    
    rows,cols = map(int, input("Enter the dimensions of the grid 'rows cols' -> e.g. '6 7': ").split()) # additional dimension options should be added later
    if rows < 4 and cols < 4:
        for i in range(3):
            rows,cols = map(int, input("Enter higher dimensions of at least 4x4 --> 'rows cols' -> e.g. '6 7': ").split())
            if rows >=4 and cols>=4:
                break
        else:
            print("Did not enter a suficient size")
            game_on = bool(int(input("Restart : 1 --> Yes , 0 --> No : ")))
            continue

    grid = grid_init(rows,cols)
    shape1 = input("Enter your token shape player 1: ")
    shape2 = input("Enter your token shape player 2: ")
    print("-------Here is the base grid--------")
    show_grid(grid)
    round = 0
    Empty_slots = [(r,c) for r in range(rows) for c in range(cols)]
    Filled_slots = []
    # Once all needed variables are initialized, the core game mechanic starts
    while True:
        round += 1
        print(f"Round {round}")

        # Player 1
        column_to_drop = int(input(f"Player1: choose a column to drop into: {[x+1 for x in list(range(cols))]} ")) - 1 
        if  column_to_drop < 0 or column_to_drop > list(range(cols))[-1]:
            while True:
                column_to_drop = int(input(f"Player1: choose a correct column to drop into: {[x+1 for x in list(range(cols))]} ")) - 1 
                if  column_to_drop >= 0 and column_to_drop <= list(range(cols))[-1]:
                     break
        
        grid = find_slot(grid,shape1, rows, column_to_drop)
        show_grid(grid)

        #Player 2
        column_to_drop = int(input(f"Player2: choose a column to drop into: {[x+1 for x in list(range(cols))]} ")) - 1 
        if  column_to_drop < 0 or column_to_drop > list(range(cols))[-1]:
            while True:
                column_to_drop = int(input(f"Player2: choose a correct column to drop into: {[x+1 for x in list(range(cols))]} ")) - 1 
                if  column_to_drop >= 0 and column_to_drop <= list(range(cols))[-1]:
                     break

        grid = find_slot(grid,shape2, rows, column_to_drop)
        show_grid(grid)

        # After both the players' turns to preserve exact movements of both in a list, but would require the player to play then the result to be shown
        status = check_filled_slots(Filled_slots, (rows,cols))

        if status:
            break

    game_on = bool(int(input("Restart : 1 --> Yes , 0 --> No : ")))
else:
    print("No Game Energy")









