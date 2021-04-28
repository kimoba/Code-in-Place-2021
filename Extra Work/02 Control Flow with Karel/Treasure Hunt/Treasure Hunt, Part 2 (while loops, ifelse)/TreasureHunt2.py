from karel.stanfordkarel import *

"""
File: TreasureHunt2.py
------------------------------
Karel will move forward until a beeper.
At every beeper, Karel will turn left and move until the next beeper, until Karel is standing on the treasure, which is a pile of 10 beepers.
"""

def main():
    while no_beepers_present():
        move_to_beeper()  # moves to beeper
        pick_beeper()  # picks up beeper
        check_direction() # if left is clear go left, otherwise turn right

    while beepers_present():
        pick_beeper()

# karel keeps moving until she encounters a beeper
def move_to_beeper():
    while no_beepers_present():
            move()

# karel checks for walls
def check_direction():
    if left_is_clear():
        turn_left()
    else:
        turn_right()

# mimics turning right by turning left 3 times
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
