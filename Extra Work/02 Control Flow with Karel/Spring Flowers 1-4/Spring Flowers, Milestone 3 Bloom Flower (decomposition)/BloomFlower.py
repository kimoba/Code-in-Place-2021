from karel.stanfordkarel import *

"""
File: BloomFlower.py
------------------------------
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""
def climb_stem():
    while right_is_blocked():
        move()

def move_to_wall():
    while front_is_clear():
        move()

def bloom():
    put_beeper()
    move()
    for i in range(2):
        turn_right()
        put_beeper()
        move()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

def main():
    # Karel will scale the stem, place 4 beepers to bloom on top, and drop down the stem facing east
    turn_left()
    climb_stem()
    bloom()
    move_to_wall()
    turn_left()

if __name__ == "__main__":
    run_karel_program()
