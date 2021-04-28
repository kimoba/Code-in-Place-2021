from karel.stanfordkarel import *

"""
File: TreasureHunt1.py
------------------------------
Karel will move forward until a beeper.
At every beeper, Karel will turn left and move until the next beeper, until Karel is standing on the treasure, which is a pile of 10 beepers.
"""

def main():
    while no_beepers_present():
        move_to_beeper()  # moves to beeper
        pick_beeper()  # picks it up
        turn_left()  # turns left

    while beepers_present():  # for the last treasure - karel will pick all of it up
        pick_beeper()

# karel will move until she gets to a beeper
def move_to_beeper():
    while no_beepers_present():
        move()

if __name__ == "__main__":
    run_karel_program('TreasureHunt1.w')
