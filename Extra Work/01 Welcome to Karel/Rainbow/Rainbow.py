from karel.stanfordkarel import *

"""
File: Rainbow.py
------------------------------
Karel makes a rainbow!
"""

def main():
# karel will paint a corner from red thru blue then move, up until the final corner
    paint_corner(RED)
    move()
    paint_corner(ORANGE)
    move()
    paint_corner(YELLOW)
    move()
    paint_corner(GREEN)
    move()
    paint_corner(BLUE)
    move()

if __name__ == "__main__":
    run_karel_program()
