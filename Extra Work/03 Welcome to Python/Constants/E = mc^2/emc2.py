# define CONSTANTS
C = 299792458

def main():
    # get user input for mass
    mass = float(input("Enter kilos of mass: "))
    joules = mass * (C**2)
    # some basic formula info + output
    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(joules) + " joules of energy!") #  print(str(mass * (C**2)) + " joules of energy!")

    # alternative shorter way to write output
    # print(f"e = m * C^2...\nm = {mass} kg\nC = {str(C)} m/s\n{mass * (C**2)}")

if __name__ == "__main__":
    main()
