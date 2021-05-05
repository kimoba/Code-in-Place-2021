"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    num_sum = num1 + num2

    # print question
    print("What is " + str(num1) + " + " + str(num2) + "?")
    user_num = int(input())  # asks user for input and cast it into integer
    if user_num == (num1 + num2):  # checks to see if user input matches num1 + num2
        print("Correct!")
    else:
        print("Incorrect. The expected answer is " + str(num_sum))
    

if __name__ == '__main__':
    main()
