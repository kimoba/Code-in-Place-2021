from karel.stanfordkarel import *

"""
File: LabyrinthKarel.py
------------------------------
Karel solves labyrinths!
"""

def main():
    # karel attempts to solve a labyrinth
    while front_is_clear():
        move_to_wall()
        find_direction()

# moves karel to the wall
def move_to_wall():
    while front_is_clear():
        move()

# find direction to turn if karel is blocked; if both left and right are blocked she won't turn
def find_direction():
    if left_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()

# turn left 3x to "turn right"
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('Labyrinth1')
