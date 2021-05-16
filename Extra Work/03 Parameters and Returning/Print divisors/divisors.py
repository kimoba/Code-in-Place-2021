def print_divisors(num):
    # delete the pass statement below and write your code!
    '''
    prints all of nums divisors
    that is, numbers that num can be divided by
    that do not have a remainder
    '''
    print(f"Here are the divisors of {num}")
    for i in range(num):
        current_divisor = i + 1
        if num % current_divisor == 0:
            print(current_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == "__main__":
    main()
