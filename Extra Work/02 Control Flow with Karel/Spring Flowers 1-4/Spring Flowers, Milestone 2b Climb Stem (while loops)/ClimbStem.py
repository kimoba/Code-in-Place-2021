from karel.stanfordkarel import *

"""
File: ClimbStem.py
------------------------------
Karel will climb a "stem" -- Karel should start facing a wall. Karel will turn and scale the wall until there is no more wall to Karel's right.
"""

def main():
    # karel moves up the stem, to where a bloom would start
    turn_left()
    while right_is_blocked():
        move()

if __name__ == "__main__":
    run_karel_program()
