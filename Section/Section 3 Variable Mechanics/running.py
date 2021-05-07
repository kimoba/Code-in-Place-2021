"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

SENTINEL = 0

def main():
    num_total = 0

    # prompt user to enter num
    num = int(input("Enter a value: "))

    # prints running total until user enters 0
    while num != SENTINEL:
        // check_min_max()
        num_total = print_total(num, num_total)
        num = int(input("Enter a value: "))



def print_total(num, num_total):
    num_total += num
    print(f"Running total is {num_total}")
    print("")
    return num_total

if __name__ == '__main__':
    main()
