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
    action()

    # print(f"TEST PLAYER INFO:\n {player_info}")
    # player_info["image"].show()

'''
player action
player can choose to
1 - check their stats
2 - train their stats
3 - go on a walk and maybe get lucky?
4 - quit program
'''
def action():
    choice = int(input("What would you like to do? \n [ 1 - check stats | 2 - train | 3 - go on a walk | 4 - quit] \n"))
    if choice == 1:  # check stats
        show_stats(player_info["name"], player_info["color"], player_info["inte"], player_info["spd"], player_info["lck"])

    elif choice == 2:  # train
        train(player_info["inte"], player_info["spd"], player_info["lck"])
    elif choice == 3:  # go on a walk
        walk(player_info["inte"], player_info["spd"], player_info["lck"])
    elif choice == 4:
        print("Thank you for playing!")
    else:
        print("Not a valid choice! Try again.")
        action()

# makes sure player stats don't go under 0 or over 100
def stat_verify(spd, inte, lck):
    if spd < 0:
        player_info["spd"] = 0
    elif inte < 0:
        player_info["inte"] = 0
    elif lck < 0:
        player_info["lck"] = 0
    elif spd > 100:
        player_info["spd"] = 100
    elif inte > 100:
        player_info["inte"] = 100
    elif lck > 100:
        player_info["lck"] = 100
    # test
    # print(f"verifying stats:\nplayer spd = {player_info['spd']}\nplayer inte = {player_info['inte']}\nplayer lck = {player_info['lck']}")

# player can go on a walk and increase or decrease their luck!
def walk(inte, spd, lck):
    player_luck = player_info["lck"] * .01

    # don't want the player to always get the good or bad results
    if player_luck == 1:
        player_luck = 0.90
    elif player_luck == 0:
        player_luck = 0.25

    event_num = random.randint(1, 2)

    # good events
    if random.random() < player_luck:
        if event_num == 1:
            lck_inc = random.randint(1, 5)
            print(f"You got a lot of pets on your walk today — feeling pretty lucky!\nLuck increased by {lck_inc}! ➕")
            print("")
            player_info["lck"] = lck + lck_inc
        else:
            lck_inc = random.randint(1, 5)
            print(f"For some reason, your walk route had a lot of free treats!\nLuck increased by {lck_inc}! ➕")
            print("")
            player_info["lck"] = lck + lck_inc
    # bad events
    else:
        if event_num == 1:
            lck_dec = random.randint(1, 5)
            print(f"Oh no! You were shooed away while trying to sneak a treat from a shop!\nLuck decreased by {lck_dec}! ➖")
            print("")
            player_info["lck"] = lck - lck_dec
        # random super lucky event if they're unlucky
        elif lck < 10 and random.random() < 0.6:
            lck_inc = random.randint(5, 10)
            print(f"For some inexplicable reason you feel super lucky!\nLuck increased by {lck_inc}! ➕")
            print("")
            player_info["lck"] = lck + lck_inc
        else:
            lck_dec = random.randint(1, 5)
            print(f"Oh no! While walking, a car passed by and got water splashed onto you!\nLuck decreased by {lck_dec}! ➖")
            print("")
            player_info["lck"] = lck - lck_dec
    stat_verify(player_info["spd"], player_info["inte"], player_info["lck"])
    action()

# player can randomly train their inte or spd, based on their luck
def train(inte, spd, lck):
    player_luck = player_info["lck"] * .01
    event_num = random.randint(1, 2)

    # random events based on player luck %
    if random.random() < player_luck:
        #print("player luck: " + player_luck)
        #print("event_num: " + event_num)
        #print("player luck value! lucky!")
        if event_num == 1:
            spd_inc = random.randint(1, 5)
            print(f"You decided to work on your running speed!\nYour speed increased by {spd_inc}! ➕")
            print("")
            player_info["spd"] = spd + spd_inc
        else:  # randint 3
            inte_inc = random.randint(1, 5)
            print(f"You decided to study some humans and their behaviors.\nYour intelligence increased by {inte_inc}! ➕")
            player_info["inte"] = inte + inte_inc
            print("")
    else:
        #print("not player luck value! unlucky!")
        if event_num == 1:
            spd_dec = random.randint(1, 5)
            print(f"Oh no, you wore yourself out trying to increase your running speed!\nYour speed decreased by {spd_dec}! ➖")
            player_info["spd"] = spd - spd_dec
            print("")
        else:
            inte_dec = random.randint(1, 5)
            print(f"You're starting to wonder if studying humans is making you dumber!\nYour int decreased by {inte_dec}! ➖")
            player_info["inte"] = inte - inte_dec
            print("")
    stat_verify(player_info["spd"], player_info["inte"], player_info["lck"])
    action()

# prints out all of the player's stats
def show_stats(name, color, inte, spd, lck):
    print("")  # empty line before showing stats
    #name & fur color
    print(f"Your stats are as follows: \n")
    print(f"NAME: {name}\nFUR COLOR: {color}")
    #intelligence
    if inte <= 25:
        print("INTELLIGENCE: Smarts could be worked on! 😅")
    elif inte <= 50:
        print("INTELLIGENCE: Average. 🙂")
    elif inte <= 75:
        print("INTELLIGENCE: So smart! 🧠")
    else:
        print("INTELLIGENCE: 🧠 You're a genius! 🧠")
    #speed
    if spd <= 25:
        print("SPEED: Slow... 😅")
    elif spd <= 50:
        print("SPEED: Average. 🙂")
    elif spd <= 75:
        print("SPEED: Fast! 💨")
    else:
        print("SPEED: 💨 Blazing fast! 💨")
    #luck
    if lck <= 25:
        print("LUCK: Not so lucky... 😅")
    elif lck <= 50:
        print("LUCK: Average luck. 🙂")
    elif lck <= 75:
        print("LUCK: Pretty lucky! 🍀 ")
    else:
        print("LUCK: 🍀 Phenomenally lucky!! 🍀")
    print("")  # empty line
    player_info["image"].show()
    action()

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
