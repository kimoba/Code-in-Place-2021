"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""

# line1: Ask a yes or no question: Is Karel male?
# line2: Only Karel knows

import random


# write all the possible answers
ANSWER_1 = "I cant understand, could you type that again?"
ANSWER_2 = "Probably no"
ANSWER_3 = "I dont know maybe you can help?"
ANSWER_4 = "Only Karel knows."
ANSWER_5 = "I'm not so sure."



# write function that prints the answers

def one_answer_generater():
    answer_number = random.randint(1, 5)
    if answer_number == 1:
        print(ANSWER_1)
    if answer_number == 2:
        print(ANSWER_2)
    if answer_number == 3:
        print(ANSWER_3)
    if answer_number == 4:
        print(ANSWER_4)
    if answer_number == 5:
        print(ANSWER_5)

def main():
    # Fill this function out!
    
    # ask user a question
    
    question = input("Ask a yes or not question: ")
#  ==
    while question != "":
        one_answer_generater()
        question = input("Ask a yes or not question: ")

    
    


    # implement loop

if __name__ == "__main__":
    main()
