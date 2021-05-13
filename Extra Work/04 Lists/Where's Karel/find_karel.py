SAMPLE_ROSTER = ['miranda', 'karel', 'shrek', 'donkey']

def find_karel(roster):
    """
    Prints whether or not Karel is in the roster.
    >>> find_karel(['chris', 'mehran'])
    Karel isn't here.
    >>> find_karel(['karel', 'is', 'here'])
    Karel is here!
    """
    for i in range(len(roster)):
        if roster[i] == 'karel':
            return print("Karel is here!")
    return print("Karel isn't here.")

def main():
    # delete the pass statement below and write your code here!
    find_karel(SAMPLE_ROSTER)

if __name__ == "__main__":
    main()
