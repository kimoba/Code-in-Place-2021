from karel.stanfordkarel import *

"""
File: TensKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():
    # place 10 beepers and move to wall
    put_10_beepers()
    while front_is_clear():
        move()
        put_10_beepers()


def put_10_beepers():
    for i in range(10):
        put_beeper()

if __name__ == "__main__":
    run_karel_program('TensKarel1.w')
