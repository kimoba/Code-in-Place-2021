from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Turn left until Karel is facing a wall.
"""

def turn_till_face_wall():
    while front_is_clear():
        turn_left()

def main():
    """
    Karel will keep turning left until she's facing a wall.
    """
    turn_till_face_wall()

if __name__ == "__main__":
    run_karel_program()
