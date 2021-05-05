"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    # intro
    print("This program subtracts one number from another.")
    # get user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # show output
    print("The result is " + str(num1 - num2))

if __name__ == '__main__':
    main()
