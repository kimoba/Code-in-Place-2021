from karel.stanfordkarel import *

"""
File: SpringFlowers.py
------------------------------
Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
"""
def main():
    # karel will scale the stems and make the flowers boom
    for i in range(2):
        move_to_wall()
        flower_bloom()
    move_to_wall()

def flower_bloom():
    scale_stem()
    bloom()
    move_to_wall()
    turn_left()

# moves karel to the nearest wall
def move_to_wall():
    while front_is_clear():
        move()

# karel climbs the flower stem
def scale_stem():
    turn_left()
    while right_is_blocked():
        move()

# mimics turning right by turning left 3 times
def turn_right():
    for i in range(3):
        turn_left()

# karel puts down 4 beepers in a square shape
# mimicing a flower
def bloom():
    put_beeper()
    move()
    for i in range(2):
        put_beeper()
        turn_right()
        move()
    put_beeper()

if __name__ == "__main__":
    run_karel_program('SpringFlowers1.w')
