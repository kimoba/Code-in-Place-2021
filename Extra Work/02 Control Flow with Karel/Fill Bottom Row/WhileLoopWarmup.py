from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Fill the entire bottom row of the world with beepers.
"""

def main():
    # fills the bottom row with beepers
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

if __name__ == "__main__":
    run_karel_program()
