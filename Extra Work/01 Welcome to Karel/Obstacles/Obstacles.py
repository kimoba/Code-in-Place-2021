from karel.stanfordkarel import *

"""
File: Obstacles.py
------------------------------
Karel will jump over the obstacles and put beepers in the pink squares.
"""

def main():
    move()
    jump_and_put_beeper()
    for i in range(2):
        ascend()
        put_beeper_in_pink()
    turn_right()
    turn_around()
    move_to_wall()

def ascend():
    turn_around()
    move()
    turn_right()

def jump_and_put_beeper():
    jump_obstacle()
    put_beeper_in_pink()

def put_beeper_in_pink():
    move()
    turn_right()
    move()
    put_beeper()

def jump_obstacle():
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

if __name__ == "__main__":
    run_karel_program()
