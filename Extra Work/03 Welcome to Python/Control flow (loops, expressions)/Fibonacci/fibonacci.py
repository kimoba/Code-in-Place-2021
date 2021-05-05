# define max term
MAX_TERM = 10000

def main():
    curr_term = 0  # current term
    next_term = 1  # adds one, next term
    while curr_term <= MAX_TERM:
        print(curr_term)  # 0
        term_after_next = curr_term + next_term  # new variable = 0 + 1
        curr_term = next_term  # change 0 to 1
        next_term = term_after_next  # change 1 to 1
        
if __name__ == "__main__":
    main()
