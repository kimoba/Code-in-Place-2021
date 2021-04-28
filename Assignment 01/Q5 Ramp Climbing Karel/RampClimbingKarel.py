from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def main():
    """
    Karel will place a beeper down, move with a slope of 1/2, and place another beeper.
    She'll continue to do so until she hits the wall.
    """
    while front_is_clear():
        put_beeper()
        slope_move()
        turn_right()
    put_beeper()  # places a beeper down if the front isn't clear

# Karel will move two squares east, face north, and move one square north


def slope_move():
    move()
    move()
    turn_left()
    move()

# imitates turning right


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program('RampKarel3.w')
