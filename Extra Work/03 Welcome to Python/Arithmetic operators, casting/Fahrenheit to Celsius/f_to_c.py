def main():
    # get user input for farenheit value
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    # farenheit to celsius formula
    degrees_celsius = (degrees_fahrenheit - 32) * 5/9

    # output F -> C
    print("Temperature: " + str(degrees_fahrenheit) + "F" + " = " + str(degrees_celsius) + "C")
    # print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

if __name__ == "__main__":
    main()
