from simpleimage import SimpleImage
import random

'''
player_info will contain:
name, color, intelligence (inte), speed (spd), and luck (lck)
'''
player_info = {}

dog_icon_og = SimpleImage("/home/dog_face_kimedit.png")

def main():
    dog_icon = clone_dog_img(dog_icon_og)

    get_player_info(dog_icon)
    action(player_info["name"], player_info["color"], player_info["inte"], player_info["spd"], player_info["lck"])

    print(f"TEST PLAYER INFO:\n {player_info}")
    player_info["image"].show()


def action(name, color, inte, spd, lck):
    choice = int(input("What would you like to do? \n [ 1 - check stats | 2 - train | 3 - go on a walk] \n"))
    if choice == 1:  # check stats
        print(f"{name}, your stats are as follows: \n")
        #inte
        if inte <= 25:
            print("INTELLIGENCE: Smarts could be worked on! 😅")
        elif inte <= 50:
            print("INTELLIGENCE: Average. 🙂")
        elif inte <= 75:
            print("INTELLIGENCE: So smart! 🧠")
        else:
            print("INTELLIGENCE: 🧠 You're a genius! 🧠")
        #spd
        if spd <= 25:
            print("SPEED: Slow... 😅")
        elif spd <= 50:
            print("SPEED: Average. 🙂")
        elif spd <= 75:
            print("SPEED: Fast! 💨")
        else:
            print("SPEED: 💨 Blazing fast! 💨")
        #lck
        if lck <= 25:
            print("LUCK: Not so lucky... 😅")
        elif lck <= 50:
            print("LUCK: Average luck. 🙂")
        elif lck <= 75:
            print("LUCK: Pretty lucky! 🍀 ")
        else:
            print("LUCK: 🍀 Phenomenally lucky!! 🍀")

# generates random int, spd, and lck stats for the player
def gen_random_stats():
    player_info["inte"] = random.randint(0, 100)
    player_info["spd"] = random.randint(0, 100)
    player_info["lck"] = random.randint(0, 100)

'''
check_color_satisfied(dog_icon):
checks to make sure if player is satisified with their color choice
otherwise asks them again to pick a fur color
also resets/copies the original dog image so we can change the default color again
'''
def check_color_satisfied(dog_icon, color):
    confirm = input("Are you satisfied? (Y/N) \n")
    print("")  # extra line after user input
    confirm = confirm.lower()
    # print(confirm)
    if confirm not in ("y", "yes"):
        dog_icon = clone_dog_img(dog_icon_og)
        get_color(dog_icon)
    else:
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
    player_info["image"] = dog_icon
    check_color_satisfied(dog_icon, color)

# checking if inputted player color is valid
def check_color(color):
    while color not in ("red", "yellow", "brown", "white", "black" ):
        print("Please enter a valid color choice! \n")
        color = input("What color is your fur? \n Pick between:\n ( red | yellow | brown | white | black )\n")
    player_info["color"] = color
    return color

# get player fur color and add it into player status dictionary
# edit dog icon to specified color
def get_color(dog_icon):
    color = input("What color is your fur? \n Pick between:\n ( red | yellow | brown | white | black )\n")
    print("")  # empty line after player input
    color = color.lower()
    color = check_color(color)
    color_dog(color, dog_icon)
    

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
    name = input("Hi there. What is your name? ")
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
    player_info["name"] = name

# get player name, color, random stats - add to dict as well
def get_player_info(dog_icon):
    get_name()
    get_color(dog_icon)
    gen_random_stats()

if __name__ == '__main__':
    main()
