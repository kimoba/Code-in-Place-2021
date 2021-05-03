"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
# aske the  user about their wight on Earth
# 37.8%
# wight*0.378
# print wight on Mars

# int number 3
# float number with decimals 3.78
def main():
    weight_earth = input("You weight on Earth: ")

    weight_earth_float = float(weight_earth)

    weight_mars = weight_earth_float * 0.378

    weight_mars_str = str(weight_mars)

    print("You weight on Mars is: " + weight_mars_str)







#     question_weight()
    
# def question_weight():
#     weight = input('What is your weight?')
#     weightOnMars = weight * 0.378
#     print(weightOnMars)
    

    

if __name__ == "__main__":
    main()
