from karel.stanfordkarel import *

"""
File: SlotsKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():
    # karel will put a beeper at each slot of the bottom row
    while front_is_clear():
        deposit_bottom_beeper()
        if front_is_blocked():
            go_back_up()
            next_row()
    deposit_bottom_beeper()  # last row

# moves to next column
def next_row():
    turn_right()
    move()

# brings karel back from the bottom row
def go_back_up():
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()

# karel moves to the bottom of the column and drops off a beeper
def deposit_bottom_beeper():
    turn_right()
    while front_is_clear():
        move()
    put_beeper()

# karen turns left 3 times to mimic turning right
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('Slots.w')
