def print_multiple(message, repeats):
    # delete the pass statement below and write your code here!
    # message to print that repeats x number of times
    for i in range (repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()

