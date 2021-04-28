from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""


def main():
    """
    Karel will pick up the puzzle piece near here, place it in the empty space within the puzzle, and return to her starting position.
    """
    move_pick_puzzle_piece(
    )  # Move to and pick up the last puzzle piece (the beeper in row 1, column 3)
    finish_puzzle()  # Put the puzzle piece in place (row 3, column 4)
    go_home()  # Return Karel to her initial position


def move_pick_puzzle_piece():
    move()
    move_pick_beeper()


def finish_puzzle():
    move()
    turn_left()
    move()
    move_put_beeper()


def go_home():
    turn_left()
    turn_left()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_pick_beeper():
    move()
    pick_beeper()


def move_put_beeper():
    move()
    put_beeper()


if __name__ == '__main__':
    run_karel_program('Puzzle.w')
