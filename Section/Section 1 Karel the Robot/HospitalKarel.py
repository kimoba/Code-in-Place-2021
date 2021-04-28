from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem

# makes Karel turn left twice to mimic turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Karel will construct the hospital 3 beepers high
# then build the next column, going down
def build_hospital():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right()
    move()
    turn_right()
    for i in range(2):
        put_beeper()
        move()
    put_beeper()

def main():
    """
    Karel keeps walking, and if she finds a beeper/supplies, she'll construct a hospital.
    Then she'll go back down and continue the cycle until she reaches the end.
    """
    while front_is_clear():
        if beepers_present():
            build_hospital()
            turn_left()
        move()


if __name__ == '__main__':
    run_karel_program('HospitalKarel2.w')
