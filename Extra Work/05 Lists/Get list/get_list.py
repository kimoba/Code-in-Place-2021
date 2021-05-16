def main():
    list = []

    entry = input("Enter a value: ")
    while entry != "":
        list.append(entry)
        entry = input("Enter a value: ")
    print("Here's the list: ", list)

if __name__ == "__main__":
    main()
