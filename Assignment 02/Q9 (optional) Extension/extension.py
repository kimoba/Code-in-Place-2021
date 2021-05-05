"""
Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
Shows how many steps it took to reach one.
"""
HAILSTONE = 1

import random 

def main():
    # get user input. make sure it's an integer
    num = int(input("Enter a num: "))
    steps = 0

    # if n is even, divide it by 2
    while num != HAILSTONE:
        if num % 2 == 0:
            new_num = int(num/2)
            print(f"{num} is even, so I take half: {new_num}")
            num = new_num
            steps += 1  # add 1 to step counter
        # if n is odd, multiply by 3 and add 1
        elif num % 2 != 0:
            new_num = int((num * 3) + 1)
            print(f"{num} is odd, so I take 3n+1: {new_num}")
            num = new_num
            steps += 1  # add 1 to step counter
    print(f"The process took {steps} to reach 1")


if __name__ == "__main__":
    main()
