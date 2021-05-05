AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)  # asks user to input affirmation
    user_feedback = input()  # get user input
    while user_feedback != AFFIRMATION:  # program will stop if user enters empty string
        print("That was not the affirmation.")  # if user input doesn't match affirmation
        print("Please type the following affirmation: " + AFFIRMATION)  # prompts again
        user_feedback = input()  # gets user input again
    print("That's right! :)")  # if user enters affirmation correctly

if __name__ == "__main__":
    main()
