from karel.stanfordkarel import *

"""
File: MoveBeeper.py
------------------------------
Karel will move the beeper up to the top of its column.
Karel starts in the bottom left corner, facing East, in front of the beeper, and Karel will end in the top right corner facing East.
"""

def main():
    """
    Karel will move to the lone beeper, pick it up, then move to the top row, place the beeper down, then move to the top right square, facing east.
    """
    find_beeper()
    pick_beeper()
    move_to_beeper_drop_location()
    put_beeper()
    move_to_destination()

# moves Karel to the beeper location
def find_beeper():
    move()

# moves Karel to the intended beeper drop location
def move_to_beeper_drop_location():
    turn_left()
    move()
    move()

# moves Karel left three times to mimic turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# moves Karel to her final destination
def move_to_destination():
    turn_right()
    move()

if __name__ == "__main__":
    run_karel_program()
