SAMPLE_LIST = ['a', 'b', 'c', 'd', 'e']
MAX_LENGTH = 3

def shorten(lst, max_len):
    # removes items from the end of the list
    while len(lst) > max_len:
        removed_item = lst.pop()
        print(removed_item)
    # prints item until lst is max_len items long
    print("The new list is: ", lst)

def main():
    shorten(SAMPLE_LIST, MAX_LENGTH)

if __name__ == "__main__":
    main()

