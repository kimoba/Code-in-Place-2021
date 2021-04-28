from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

def main():
    go_collect_newspaper()
    turn_around()
    back_to_start()

def back_to_start():
    move_to_wall()
    turn_right()
    move()
    turn_right()

def go_collect_newspaper():
    move_down_row()
    while no_beepers_present():
        move()
    pick_beeper()

def move_down_row():
    turn_right()
    move()
    turn_left()

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
