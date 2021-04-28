from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Move Karel forward until you run into a wall (don't walk through the wall!).
"""

def move_to_wall():
    while front_is_clear():
        move()

def main():
    """
    Karel moves until she hits a wall.
    """
    move_to_wall()

if __name__ == "__main__":
    run_karel_program()
