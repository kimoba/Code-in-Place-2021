from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""
# Karel will draw a Dratini from Pokemon!
def main():
    #row 1 - blank
    move_up_row()
    row_02()
    go_back_and_next_row()
    row_03()
    go_back_and_next_row()
    row_04()
    go_back_and_next_row()
    row_05()
    go_back_and_next_row()
    row_06()
    go_back_and_next_row()
    row_07()
    go_back_and_next_row()
    row_08()
    go_back_and_next_row()
    row_09()
    go_back_and_next_row()
    row_10()
    go_back_and_next_row()
    row_11()
    go_back_and_next_row()
    row_12()
    go_back_and_next_row()
    row_13()
    go_back_and_next_row()
    row_14()
    go_back_and_next_row()
    row_15()
    go_back_and_next_row()
    row_16()
    go_back_and_next_row()

def row_16():
    for i in range(2):
        move()
        paint_corner(BLACK)
    move()
    for i in range(5):
        move()
        paint_corner(BLACK)
    for i in range(3):
        move()
    for i in range(2):
        move()
        paint_corner(BLACK)

def row_15():
    paint_one_corner_black()
    move()
    paint_corner(WHITE)
    paint_one_corner_black()
    for i in range(5):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()
    move()
    paint_one_corner_black()
    move()
    paint_corner(WHITE)
    paint_one_corner_black()

def row_14():
    move()
    paint_one_corner_black()
    move()
    paint_corner(BLUE)
    for i in range(2):
        move()
        paint_corner(WHITE)
    for i in range(4):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()
    move()
    paint_corner(WHITE)
    paint_one_corner_black()

def row_13():
    move()
    paint_one_corner_black()
    for i in range(4):
        move()
        paint_corner(BLUE)
    move()
    paint_corner(WHITE)
    paint_one_corner_black()
    move()
    paint_corner(BLUE)
    for i in range(3):
        move()
        paint_corner(WHITE)
    paint_one_corner_black()

def row_12():
    paint_one_corner_black()
    for i in range(3):
        move()
        paint_corner(WHITE)
    for i in range(2):
        move()
        paint_corner(BLUE)
    for i in range(2):
        move()
        paint_corner(BLACK)
    for i in range(3):
        move()
        paint_corner(WHITE)
    for i in range(4):
        move()
        paint_corner(BLACK)

def row_11():
    paint_corner(BLACK)
    for i in range(5):
        move()
        paint_corner(WHITE)
    move()
    paint_corner(BLUE)
    for i in range(2):
        move()
        paint_corner(BLACK)
    for i in range(4):
        move()
        paint_corner(WHITE)
    paint_one_corner_black()
    move()
    paint_corner(BLUE)
    paint_one_corner_black()

def row_10():
    paint_corner(BLACK)
    for i in range(5):
        move()
        paint_corner(WHITE)
    for i in range(3):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()
    for i in range(2):
        move()
        paint_corner(WHITE)
    paint_one_corner_black()
    for i in range(2):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()

def row_09():
    paint_one_corner_black()
    for i in range(3):
        move()
        paint_corner(WHITE)
    move()
    paint_corner(BLUE)
    paint_one_corner_black()
    for i in range(2):
        move()
        paint_corner(BLUE)
    for i in range(3):
        move()
        paint_corner(BLACK)
    for i in range(3):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()

def row_08():
    move()
    paint_one_corner_black()
    for i in range(6):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()
    for i in range(5):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()

def row_07():
    for i in range(2):
        move()
    paint_one_corner_black()
    for i in range(2):
        move()
        paint_corner(WHITE)
    for i in range(4):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()
    for i in range(4):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()


def row_06():
    for i in range(2):
        move()
    paint_one_corner_black()
    for i in range(4):
        move()
        paint_corner(WHITE)
    for i in range(6):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()

def row_05():
    for i in range(2):
        move()
    paint_one_corner_black()
    for i in range(5):
        move()
        paint_corner(WHITE)
    for i in range(5):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()

def row_04():
    for i in range(3):
        move()
    paint_one_corner_black()
    for i in range(4):
        move()
        paint_corner(WHITE)
    for i in range(4):
        move()
        paint_corner(BLUE)
    paint_one_corner_black()

def row_03():
    for i in range(3):
        move()
    for i in range(2):
        move()
        paint_corner(BLACK)
    for i in range(4):
        move()
        paint_corner(WHITE)
    move()
    paint_corner(BLUE)
    for i in range(2):
        move()
        paint_corner(BLACK)

def row_02():
    for i in range(5):
        move()
    for i in range(5):
        move()
        paint_corner(BLACK)

def paint_one_corner_black():
    move()
    paint_corner(BLACK)

# moves back to column 1 and up to the next row
def go_back_and_next_row():
    go_back()
    move_up_row()

# pre: face east. post: face east
def go_back():
    for i in range(2):
        turn_left()
    go_to_wall()
    for i in range(2):
        turn_right()

def go_to_wall():
    while front_is_clear():
        move()

# pre: face East. post: face East.
def move_up_row():
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('dratini.w')
