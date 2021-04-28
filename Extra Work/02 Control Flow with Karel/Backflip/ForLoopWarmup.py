from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Get Karel to do a cool backflip by turning left 4 times.
"""

def backflip():
    for i in range(4):
        turn_left()

def main():
    """
    Karel will perform a backflip by turning left 4 times.
    """
    backflip()

if __name__ == "__main__":
    run_karel_program()
