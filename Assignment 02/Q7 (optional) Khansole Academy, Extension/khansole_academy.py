"""
This program will ask the user the sum of
two randomly generated numbers until
they get 3 in a row correct!
"""

import random

CORRECT_IN_A_ROW = 3

def main():
    # define starting value for correct count
    correct_count = 0

    while correct_count != CORRECT_IN_A_ROW:
        # generate two random numbers and their sum
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        num_sum = num1 + num2

        # ask user for sum of 2 randomly generated numbers
        print("What is " + str(num1) + " + " + str(num2) + "?")
        # get user input
        user_input = input()
        user_input = int(user_input)  # cast user input into an int
        # check user input
        if user_input == num_sum:  # if user input matches num_sum
            correct_count += 1  # add one to correct count
            print("Correct! You've gotten " + str(correct_count) + " correct in a row.")
            if correct_count == CORRECT_IN_A_ROW:
                # complete program
                print("Congratulations! You mastered addition.")
                # print("")  # new line
        else:
            # reset correct counter
            correct_count = 0
            # tell user the correct answer
            print("Incorrect. The expected answer is " + str(num_sum))
            # print("")  # new line

if __name__ == '__main__':
    main()
