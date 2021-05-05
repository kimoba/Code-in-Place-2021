"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""
import random

# CONSTANT ANSWERS
ANSWER_1 = "Yes!"
ANSWER_2 = "No!"
ANSWER_3 = "Maybe?"
ANSWER_4 = "Try asking again."
ANSWER_5 = "In the near future, yes."

def random_answer():
    # pick a random num between 1 thru 5
    random_num = random.randint(1, 5)
    # each num is tied to a diff answer:
    if random_num == 1:
        print(ANSWER_1)
    elif random_num == 2:
        print(ANSWER_2)
    elif random_num == 3:
        print(ANSWER_3)
    elif random_num == 4:
        print(ANSWER_4)
    else:
        print(ANSWER_5)

def main():
    while input != "":  # keeps asking the user to ask a y/n question
        input("Ask a yes or no question: ")
        random_answer()  # spits out a random answer
        print("")  # extra line for formatting


if __name__ == "__main__":
    main()
