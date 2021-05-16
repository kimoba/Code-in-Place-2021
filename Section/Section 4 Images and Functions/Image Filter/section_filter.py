"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

BRIGHT_VALUE = 153

def main():
    image = SimpleImage('images/simba-sq.jpg')

    # Apply the filter
    # TODO: your code here
    for pixel in image:
        pixel_avg = get_pixel_avg(pixel)
        # print(pixel_bright_enough)
        if pixel_avg > BRIGHT_VALUE:
            pixel.red = pixel_avg
            pixel.green = pixel_avg
            pixel.blue = pixel_avg

    image.show()

def get_pixel_avg(pixel):
    return (pixel.red + pixel.green + pixel.blue) // 3

if __name__ == '__main__':
    main()
