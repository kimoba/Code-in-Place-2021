from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Clean a spot by picking up beepers until there aren't any left.
"""

def clean_spot():
    while beepers_present():
        pick_beeper()

def main():
    """
    Karel will keep picking up beepers until there are none left.
    """
    clean_spot()

if __name__ == "__main__":
    run_karel_program()
