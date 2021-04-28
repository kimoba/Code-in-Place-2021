from karel.stanfordkarel import *

"""
File: SafePickup.py
--------------------
When you finish writing this file, Karel should be able to
pick up a beeper from the current position if one is present
(but do nothing if no beepers are present).
"""


def main():
    """
    If there is a beeper where Karel is, she'll pick it up - otherwise, she does nothing.
    """
    if beepers_present():
        pick_beeper()


if __name__ == '__main__':
    run_karel_program('SafePickup1.w')
