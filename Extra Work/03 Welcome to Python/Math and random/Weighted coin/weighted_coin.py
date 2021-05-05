import random
# define CONSTANT
HEADS_WEIGHT = 0.7 # 70% chance of heads

def main():
    if random.random() < HEADS_WEIGHT:  # random.random() returns a random floating num between 0 and 1
        print("Heads!")  # 70% of heads
    else:
        print("Tails!")  # 30% of tails

if __name__ == "__main__":
    main()
