# define constant
MIN_HEIGHT = 50

def main():
    # get user input for their height
    user_height = input("How tall are you? ")
    while user_height != "":  # if the user enters 'nothing' the string will be empty, "" and the program will be done
        user_height = float(user_height)
        if user_height >= MIN_HEIGHT:  # height check
            print("You're tall enough to ride!")  # if user height is >= min height
        else:
            print("Sorry, you're not tall enough to ride!")  # if user height is < min height
        user_height = input("How tall are you? ")  # asks the question again

if __name__ == "__main__":
    main()
