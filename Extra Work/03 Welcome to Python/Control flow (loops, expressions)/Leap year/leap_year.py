def main():
    print("This program will check if a year is a leap year.")
    year = int(input("Please enter a year: "))  # user inputted year cast into INT

    # year must be divisible by 4
    # if the year can be divided by 100, it's not a leap year
    # UNLESS the year is also divided by 400

    #if (year % 4 == 0):  # check if divisible by 4 | note: no remainders after dividing
        #print("This is a leap year!")
    #elif (year % 100 == 0):  # check if divisible by 100
        #if (year % 400 == 0):  # check if also divisible by 400 after 100
            #print("This is a leap year!")
        #else:
            #print("This is not a leap year!")
    #else:  # check if not divisible by 4 or 100
        #print("This is not a leap year!")

    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("This is a leap year!")  # divisible by 4, 100, and 400
            else:
                print("This is not a leap year!")  # divisible by 4 and 100 but not 400
        else:
            print("This is a leap year!")  # divisible by 4
    else:
        print("This is not a leap year!")

if __name__ == "__main__":
    main()
