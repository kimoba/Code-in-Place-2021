from simpleimage import SimpleImage
player_info = {}
dog_icon_og = SimpleImage("/home/dog_face_kimedit.png")

def main():
    dog_icon = clone_dog_img(dog_icon_og)

    player_info["name"] = get_name()
    player_info["color"] = get_color(dog_icon)

    print(f"TEST PLAYER INFO:\n {player_info}")


'''
check_color_satisfied(dog_icon):
checks to make sure if player is satisified with their color choice
otherwise asks them again to pick a fur color
also resets/copies the original dog image so we can change the default color again
'''
def check_color_satisfied(dog_icon, color):
    confirm = input("Are you satisfied? (Y/N) \n")
    confirm = confirm.lower()
    # print(confirm)
    if confirm not in ("y", "yes"):
        dog_icon = clone_dog_img(dog_icon_og)
        get_color(dog_icon)
    print("Sounds good!\n")

'''
color_dog(color, dog_icon):
edit dog icon to specified color

original image credit: Cartoon Vectors by Vecteezy User nightwolfdezines
https://www.vecteezy.com/vector-art/581279-dog-faces-pixel-art-icons

replaces default image color values: R 242 G 179 B 106 with player choice of color
but with my color choice of RGB values :)
'''
def color_dog(color, dog_icon):
    if color == "red":
        for pixel in dog_icon:
            if pixel.red == 242 and pixel.green == 179 and pixel.blue == 106:
                pixel.red = 255
                pixel.green = 110
                pixel.blue = 95
    elif color == "yellow":
        for pixel in dog_icon:
            if pixel.red == 242 and pixel.green == 179 and pixel.blue == 106:
                pixel.red = 255
                pixel.green = 236
                pixel.blue = 132
    elif color == "brown":
        for pixel in dog_icon:
            if pixel.red == 242 and pixel.green == 179 and pixel.blue == 106:
                pixel.red = 222
                pixel.green = 182
                pixel.blue = 139
    elif color == "white":
        for pixel in dog_icon:
            if pixel.red == 242 and pixel.green == 179 and pixel.blue == 106:
                pixel.red = 255
                pixel.green = 255
                pixel.blue = 255
    elif color == "black":
        for pixel in dog_icon:
            if pixel.red == 242 and pixel.green == 179 and pixel.blue == 106:
                pixel.red = 91
                pixel.green = 86
                pixel.blue = 86
    dog_icon.show()
    check_color_satisfied(dog_icon, color)

# checking if inputted player color is valid
def check_color(color):
    while color not in ("red", "yellow", "brown", "white", "black" ):
        print("Please enter a valid color choice! \n")
        color = input("What color is your fur? \n Pick between:\n ( red | yellow | brown | white | black )\n")
    return color

# get player fur color and add it into player status dictionary
# edit dog icon to specified color
def get_color(dog_icon):
    color = input("What color is your fur? \n Pick between:\n ( red | yellow | brown | white | black )\n")
    print("")  # empty line after player input
    color = color.lower()
    color = check_color(color)
    color_dog(color, dog_icon)
    return color

# clones original dog icon "dog_icon_og" to new canvas "dog_icon"
def clone_dog_img(dog_icon_og):
    width = dog_icon_og.width
    height = dog_icon_og.height

    dog_icon = SimpleImage.blank(width, height)

    for x in range(width):
        for y in range(height):
            pixel = dog_icon_og.get_pixel(x, y)
            dog_icon.set_pixel(x, y, pixel)
    return dog_icon

# get player name and add it into player status dictionary
def get_name():
    name = input("What is your name? ")
    print("")  # empty line after player input
    confirm = input(f"{name}? Is that right? (Y/N) ")
    confirm = confirm.lower()
    if confirm == "y" or confirm == "yes":
        print("Sounds good!\n")
    else: 
        while confirm.lower() not in ("y", "yes"):
            name = input("What is your name? ")
            confirm = input(f"{name}? Is that right? (Y/N) ")
            print("")
    return name

if __name__ == '__main__':
    main()
