from karel.stanfordkarel import *

"""
File: InvertKarel.py
-----------------------
Inverts the pattern of beepers in a single row world.
"""

def main():
    # while moving to the wall
    # karel will put beepers where there are no beepers
    # karel will pick up beepers where there are beepers
    beeper_check()
    invert_beepers()

def invert_beepers():
    while front_is_clear():
        move()
        beeper_check()

def beeper_check():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()


if __name__ == "__main__":
    run_karel_program('Invert2.w')
