from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
NUM_REPEATS = 2

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Create new SimpleImage of correct dimensions
    # TODO: FILL IN THE WIDTH AND HEIGHT BELOW
    final_image = SimpleImage.blank(image.width * NUM_REPEATS, image.height)

    for i in range(NUM_REPEATS):
        start_x = image.width * i
        place_image(image, start_x, final_image)

    # Show the repeated image
    final_image.show()


def place_image(image, start_x, final_image):
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            final_image.set_pixel(start_x + x, y, pixel)
    return final_image


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
