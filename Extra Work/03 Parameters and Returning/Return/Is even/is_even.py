def is_even(num):
    # delete the pass statement below and write your code here!
    if num % 2 == 0:
        return True

def main():
    num = int(input("Enter a number: "))
    if is_even(num):
        print("That number is even!")
    else:
        print("That number is not even!")

if __name__ == "__main__":
    main()

