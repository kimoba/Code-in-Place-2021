from karel.stanfordkarel import *

"""
File: FiveCorridorsKarel.py
-----------------------
Karel traverse 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
"""

def main():
    # Karel will move to the wall and check for beeper
    # if no beeper, put one
    # go back to the start
    check_corridor()
    # since it's 5 corridors we'll repeat these next steps 4 times
    for i in range(4):
        go_up()
        check_corridor()

def check_corridor():
    move_to_wall()
    beeper_check()
    turn_around()
    move_to_wall()
    turn_around()

# Karel will move till she hits  wall
def move_to_wall():
    while front_is_clear():
        move()

# checks if there are any beepers present
# if not, places beeper
def beeper_check():
    if no_beepers_present():
        put_beeper()

# Karel will exit the corridor
def turn_around():
    for i in range(2):
        turn_left()

def go_up():
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
