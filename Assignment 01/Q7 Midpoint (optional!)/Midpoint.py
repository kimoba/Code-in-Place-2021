from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper in the middle of the first row.
"""

def main():
    while front_is_clear():
        step_up_top_right() # pre: karel is facing East // post: karel is facing East.
    if right_is_clear(): # makes Karel face south when she reaches the world corner
        turn_right()
    while front_is_clear():
        step_down_to_mid()  # pre: karel is facing South // post: karel is facing South
    put_midpoint_beeper()

def put_midpoint_beeper():
    put_beeper()
    if left_is_clear():  # checks for 1x1 worlds; left cant be clear for 1x1 world
        turn_right()
    else:
        for i in range(2):
            turn_left()

def step_down_to_mid():
        move()
        if front_is_clear():  # checks for even worlds
            move()
        turn_right()
        move()
        turn_left()

def step_up_top_right():
    move()
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('Midpoint1.w')
