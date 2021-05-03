"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

MARS_WEIGHT_MULTIPLER = 0.378

def main():
# asks user for their weight
    weight = float(input("How much do you weigh? "))
    print("You would weigh " + str(weight * MARS_WEIGHT_MULTIPLER) + " on Mars!")

if __name__ == "__main__":
    main()
