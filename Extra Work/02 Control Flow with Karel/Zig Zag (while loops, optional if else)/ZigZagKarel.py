from karel.stanfordkarel import *

"""
File: ZigZagKarel.py
-----------------------
Places a zig zag pattern of beepers in the world.
"""

def main():
    # karel will put down beepers in a zig zag pattern throughout the world
    zig_zag()
    while front_is_clear():
        move()
        zig_zag()

"""
zig_zag()
pre-condition: karel is facing east
post-condition: karel is facing east on column 2
"""
def zig_zag():
    put_beeper()
    turn_left()
    move()
    turn_right()
    if front_is_clear():  # checks for even column worlds
        move()
        put_beeper()
    turn_right()
    move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program('ZigZag1.w')
