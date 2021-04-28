from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.
"""


def main():
    """
    Karel will keep moving east, and if there is a beeper she'll pick it up along the way.
    """
    while front_is_clear():  # if the square in front of Karel is clear, do the following:
        move_and_beeper_check()

# Karel will move a square and check for a beeper
# if a beeper exists, she'll pick it up


def move_and_beeper_check():
    move()
    if beepers_present():
        pick_beeper()


if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
