from karel.stanfordkarel import *

"""
File: UpstairsDownstairs.py
------------------------------
Karel will climb three stair steps up and then three stair steps down.
"""

def main():
    # Karel will climb 3 stairs up
    # then climb 3 stairs down
    # SOLUTION 1
    # climb_up()
    # climb_down()

    # SOLUTION 2
    # climb stairs
    while front_is_blocked():
        climb_up()
    turn_right()  # turns right so Karel faces south; precondition for descending stairs

    # descend stairs
    if right_is_clear():
        climb_up()
    turn_left()  # Karel finishes, facing East

def climb_up():
    for i in range(3):
        turn_left()
        move()
        turn_right()
        move()

def climb_down():
    for i in range(3):
        move()
        turn_right()
        move()
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('UpstairsDownstairs.w')
