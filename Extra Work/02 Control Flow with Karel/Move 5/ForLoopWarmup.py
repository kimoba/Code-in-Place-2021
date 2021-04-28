from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Move forward 5 times.
"""

def main():
    """
    Karel will move forward 5 times.
    """
    for i in range(5):
        move()

if __name__ == "__main__":
    run_karel_program()
