# define CONSTANT
ONE_HUMAN_TO_DOG_YEAR = 7.18  # 1 human year is equal to ~7.18 dog years

def main():
    human_age = float(input("Enter an age in human years: "))

    # print output
    print("That's " + str(human_age * ONE_HUMAN_TO_DOG_YEAR) + " in dog years!")
    # print(f"That's {human_age * ONE_HUMAN_TO_DOG_YEAR} in dog years!")  # alternative print statement

if __name__ == "__main__":
    main()
