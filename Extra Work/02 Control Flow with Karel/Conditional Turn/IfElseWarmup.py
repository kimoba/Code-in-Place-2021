from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
Turn based on whether or not a beeper is present.
"""
def turn_right():
    for i in range(3):
        turn_left()

def main():
    # if there's a beeper in the current spot, turn left
    # else turn right
    if beepers_present():
        turn_left()
    else:
        turn_right()

if __name__ == "__main__":
    run_karel_program('1x1Beeper.w')
