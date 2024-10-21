"""
This prject serves as the first portfolio prject Codedacdemy's Computer Science Career path
targeting the introduction to programming section via Python.

The Goal of this project is to make a terminal based user-interactive project. I have choosen the famous
Connect Four as the backbone for this project as it can be a fun project to build upon as my skillset evolves.

The basic implementation involves:
    1 - A 2 player game (A game against a CPU can be added later on)
    2 - A dynamic grid that is decided upon by the players
    3 - Each player gets to choose thier own token 
    4 - The program tracks the tokens and when 4 tokens connect in any direction then
        that player wins and that game concludes. (An Option to restart or to end to offered)
    
I have seen some resoursec where AI plays against itself to train and then can be used to play against, this 
is a very interesting concept that can be touched upon. I understand that I am not inventing new tech but hopefully this project 
enforces solid and expansive programming principles. 
"""

Rules = {1:"A 2 player game", 
2:"A dynamic grid that is decided upon by the players",
3:"Each player gets to choose thier own token",
4:"The program tracks the tokens and when 4 tokens connect in any direction then that player wins and that game concludes. (An Option to restart or to end to offered)"}


print("---------------      Connect FOUR      ---------------")

for rules in Rules.values():
    print(rules)


game_on = bool(input("Is the game on : 1 --> yes , 0 --> No : ")) 

def grid_init():
    pass

while game_on:
    pass
else:
    print("No Game Energy Left")









