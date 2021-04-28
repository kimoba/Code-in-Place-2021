from karel.stanfordkarel import *

"""
File: Archway.py
------------------------------
Karel will move up and over the archway.
"""

def main():
    # Karel will move up and over the archway
    turn_left()
    move_to_wall()
    for i in range(2):
        turn_right()
        move_to_wall()
    turn_right()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
