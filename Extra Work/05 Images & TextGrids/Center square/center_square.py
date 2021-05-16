from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
SQUARE_WIDTH = 200

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    center_square = SimpleImage.blank(SQUARE_WIDTH, SQUARE_WIDTH)

    # TODO: your code here
    print("(image.width - SQUARE_WIDTH) / 2 is ", (image.width - SQUARE_WIDTH)/2)
    print("(image.height - SQUARE_WIDTH) / 2 is ", (image.width - SQUARE_WIDTH)/2)
    starting_x = ((image.width - SQUARE_WIDTH)/2)
    starting_y = ((image.height - SQUARE_WIDTH)/2)
    
    for y in range(SQUARE_WIDTH):
        for x in range(SQUARE_WIDTH):
            # grab pixels from og image
            pixel = image.get_pixel(starting_x + x, starting_y + y)
            # test: print(pixel.x, pixel.y)
            # paste into new canvas = center_square 200 px by 200 px
            center_square.set_pixel(x, y, pixel)

    # Show the image after the transform
    center_square.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
