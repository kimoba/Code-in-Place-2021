"""
Prints out a spaceship launch sequence.
"""
def main():
    current_num = 10

    print(current_num)
    for i in range(9):
        print(current_num - 1)
        current_num -= 1
        if current_num == 1:
            print("Liftoff!")

if __name__ == '__main__':
    main()
