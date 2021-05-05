def main():
    # get number to be divided by from the user
    dividend = int(input("Please enter an integer to be divided: "))
    # get number to divide by from the user
    divisor = (int(input("Please enter an integer to divide by: ")))
    quotient = int(dividend / divisor)
    remainder = dividend % divisor

    # output
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))
    # alternative output
    # print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
