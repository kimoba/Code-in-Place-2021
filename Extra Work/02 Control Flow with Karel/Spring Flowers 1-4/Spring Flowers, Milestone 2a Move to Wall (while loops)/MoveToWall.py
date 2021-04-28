from karel.stanfordkarel import *

"""
File: MoveToWall.py
------------------------------
Karel will move until front is blocked by a wall.
"""

def main():
    #move until front is blocked
    while front_is_clear():
        move()

if __name__ == "__main__":
    run_karel_program()
