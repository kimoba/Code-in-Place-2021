"""
This program simulates the Game of Nimm
The game starts with 20 stones in a pile
Two players may take either 1 or 2 stones with alternating turns
The game ends when the losing player takes the last stone
"""

import random

def main():
    stones_left = 20
    player = "Player 1"

    while stones_left > 0:
        # game starts with 20 stones
        print(f"There are {stones_left} stones left")

        # get user input and turn it into an int
        stone_pick = int(input(f"{player} would you like to remove 1 or 2 stones? "))

        # calculate stones left after user input
        stones_left = calc_stones(stone_pick, stones_left)

        # get player 1 or 2
        player = get_player(player)

    print(f"{player} wins!")

def calc_stones(stone_pick, stones_left):
    # check if stone pick doesn't equal 1 or 2
    if stone_pick != 1 and stone_pick != 2:
        stone_pick = int(input(f"Please enter 1 or 2: "))  # ask them to enter either 1 or 2
    print("")  # empty line for both results
    
    # basic calculations to determine how many stones are left
    if stone_pick == 1:
        stones_left = (stones_left - 1)
    else:
        stones_left = (stones_left - 2)
    return stones_left

def get_player(player):
    if player == "Player 2":
        player = "Player 1"
        return player
    else:
        player = "Player 2"
        return player

if __name__ == '__main__':
    main()
