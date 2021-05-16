def print_ones_digit(num):
    # delete the pass statement below and write your code!
    print(f"The ones digit is {num % 10}")

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()
