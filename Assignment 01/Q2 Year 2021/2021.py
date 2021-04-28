from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""


def main():
    """
    Karel places down 20 beepers, moves a square forward, places down 21 beepers,
    then moves one more square facing east.
    """
    place_20_beepers()  # put down 20 beepers at starting position
    move()  # move one square forward
    place_20_beepers()  # put 20 beepers
    put_beeper()  # put that last beeper
    move()


def place_20_beepers():  # places 20 beepers
    for i in range(20):
        put_beeper()


if __name__ == '__main__':
    run_karel_program('3x3.w')
