"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(filename)

    # get height and width of image
    height = image.height
    width = image.width

    # make blank new canvas, double the height
    mirror = image.blank(width, height * 2) 

    """
    1. going to loop through each column (top to bottom)
                       x, y
    2. first pixel is (0, 0) at the top left
        2a. copy that pixel from the ORIGINAL image
        2b. paste that pixel onto the new BLANK "mirror"
            image at the same coordinates
        2c. do the same for the opposite side
            x coordinate is the same
            y is flipped (doubled height - y+1 bc the image starts at 0, 0)
    then move to the next row (left to right)
    """
    for x in range(width): 
        for y in range(height):
            pixel = image.get_pixel(x, y)  # 0, 0
            mirror.set_pixel(x, y, pixel)  # 0, 0
            mirror.set_pixel(x, (height * 2) - (y + 1), pixel)

    return mirror


def main():
    # Get file and load image
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
