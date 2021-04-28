from karel.stanfordkarel import *

"""
File: BloomFlower.py
------------------------------
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""
def turn_right():
    for i in range(3):
        turn_left()

def main():
    # bloom a flower
    # put 4 beepers in a square
    put_beeper()
    move()
    for i in range(2):
        turn_right()
        put_beeper()
        move()
    put_beeper()


if __name__ == "__main__":
    run_karel_program()
