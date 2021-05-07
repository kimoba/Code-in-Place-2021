"""
Prints the Fizz Buzz sequence up to a given number.
"""

def main():
    num_fizzed = 0
    num_buzzed = 0
    num_fizzbuzzed = 0

    # user's desired number via input
    num_count_to = int(input("Number to count to: "))
    # i counts from 1 thru 17
    for i in range(1, num_count_to + 1):
        # if divisible by 3 AND 5
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            num_fizzbuzzed += 1
        # if only divisble by 3
        elif i % 3 == 0:
            print("fizz")
            num_fizzed += 1
        # if only divisible by 5
        elif i % 5 == 0:
            print("buzz")
            num_buzzed += 1
        # if NOT divisible by 3 or 5
        else:
            print(i)
    # print how many fizz, buzz, and fizzbuzz
    print_results(num_fizzed, num_buzzed, num_fizzbuzzed)
 

def print_results(num_fizzed, num_buzzed, num_fizzbuzzed):
    print("")
    print(f"Num fizzed: {num_fizzed}")
    print(f"Num buzzed: {num_buzzed}")
    print(f"Num fizzbuzzed: {num_fizzbuzzed}")

if __name__ == '__main__':
    main()
