from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Place 10 beepers.
"""

def main():
    """
    Karel will put down 10 beepers!
    """
    for i in range(10):
        put_beeper()

if __name__ == "__main__":
    run_karel_program()
