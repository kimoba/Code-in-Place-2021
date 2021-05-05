def main():
    num_id = float(input("Type a number to see its square: "))  # asks user for a number and casts it from STR to FLOAT
    print(f"{num_id} squared is {num_id**2}")  # **2 means to the power of 2 aka squared
    # print(str(num_id) + " squared is " + str(num_id**2))  # alternative way to write print function. the float has to be cast as string

if __name__ == "__main__":
    main()
