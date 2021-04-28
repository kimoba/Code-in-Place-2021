from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.
"""

# mimics turning right by turning left two times
def turn_right():
    turn_left()
    turn_left()

# Karel will repair the column, going north from her starting point
def repair():
    turn_left()  # gotta face north
    while front_is_clear():  # makes sure the front is free
        if beepers_present():  # keep moving if a beeper already exists
            move()
        elif no_beepers_present():  # no beepers? put one down
            put_beeper()
            move()
    if front_is_blocked():  # if the front is blocked while building but no beepers, put one
        if no_beepers_present():
            put_beeper()

# Karel moves back south
def go_back():
    turn_right()  # face south
    while front_is_clear():  # keeps moving while the front is clear
        move()

# moves Karel to the next Ave
def next_ave():
    turn_left()
    for i in range(4):  # do this 4 times
        move()

def main():
    """
    Time for Karel to repair some columns!
    Every column is 3 squares apart, with no defined height.
    """
    while front_is_clear():
            repair()
            go_back()
            next_ave()
    repair()  # last column repair
    go_back()  # go back down the last column

if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
