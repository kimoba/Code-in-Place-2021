import math

def main():
    # Pythagorean Theorem
    # BC^2 = AB^2 + AC^2
    # BC = sqrt AB^2 + AC^2
    
    # get user input for triangle sides
    ab = int(input("Enter the length of AB: "))
    ac = int(input("Enter the length of AC: "))
    # use math.sqrt to find BC
    bc = math.sqrt(AB**2 + AC**2)

    #print output
    print("The length of BC (the hypotenuse) is: " + str(bc))

if __name__ == "__main__":
    main()
