"""
This program simulates the Game of Nimm
The game starts with 20 stones in a pile
Two players may take either 1 or 2 stones with alternating turns
The game ends when the losing player takes the last stone
"""

import random

def main():
    stones_left = 20
    turn = 1

    while stones_left > 0:
        # game starts with 20 stones
        print(f"There are {stones_left} stones left")

        # get player 1 or 2
        player = get_player(turn)
        turn += 1
        # print(f"note: currently on {player}'s turn")  # test

        # get choice of stones
        stone_pick = get_stone(player)
        # print(f"note: stone_pick currently equals {stone_pick}")  # test

        # calculate stones left based on player's pick
        stones_left = calc_stones(stone_pick, stones_left)
        # print(f"note: stones_left currently equals {stones_left}")  # test

    decide_winner(stone_pick)

def decide_winner(stone_pick):


def calc_stones(stone_pick, stones_left):
    if stone_pick == 1:
        stones_left -= 1
    else:
        stones_left -= 2
    return stones_left

def get_stone(player):
    # get user input and turn it into an int
    stone_pick = int(input(f"{player} would you like to remove 1 or 2 stones? "))
    # check if stone pick doesn't equal 1 or 2
    if stone_pick != 1 and stone_pick != 2:
        stone_pick = int(input(f"Please enter 1 or 2: "))  # ask them to enter either 1 or 2
    print("")  # empty line for both results
    return stone_pick  # return value

def get_player(turn):
    # if turn # is divisable by 2 then it's player 2's turn
    if turn % 2 == 0:
        player = "Player 2"
        # print(f"note: player_count is at {turn}")  # test
    else:  # else it's player 1's turn
        player = "Player 1"
        # print(f"note: player_count is at {turn}")  # test

    return player  # return player num

if __name__ == '__main__':
    main()
