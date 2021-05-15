"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random  # import random library

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for y in range(N_ROWS):
        for x in range(N_COLS):
            start_x = x * PATCH_SIZE  # 3 columns; x will be 0 * 222, 1 * 222, 2 * 222
            start_y = y * PATCH_SIZE  # 2 rows: y will be 0 * 222 then 1 * 222
            patch = make_recolored_patch(random.uniform(0, 2), random.uniform(0, 2), random.uniform(0, 2))
            # print(random.uniform(0, 2))

            # This is an example which should generate a pinkish patch
            # patch = make_recolored_patch(1.5, 0, 1.5)
            final_image = put_patch(final_image, start_x, start_y, patch)
    final_image.show()  # show final_image

    # MANUAL
    # # place a patch onto the final image
    # # with its top left corner at ( start_x , start_y )
    # # TOP ROW
    # put_patch(final_image, 0, 0, patch)  # column 1
    # put_patch(final_image, 222, 0, patch)  # column 2
    # put_patch(final_image, 444, 0, patch)  # column 3
    # # BOTTOM ROW
    # put_patch(final_image, 0, 222, patch)  # column 3
    # put_patch(final_image, 222, 222, patch)  # column 3
    # put_patch(final_image, 444, 222, patch)  # column 3

    #final_image.show()
    # patch.show()  # image recolor test. good


def put_patch(final_image, start_x, start_y, patch):
    '''
    final_image height: 444 (2 rows) Y
    final_image width: 666 (3 columns) X
    '''

    # shorter way to write this - sub pixel for patch.get_pixel(x, y)
    for y in range(patch.height):
        for x in range(patch.width):
            final_image.set_pixel(start_x + x, start_y + y, patch.get_pixel(x, y))
    return final_image

    # for y in range(patch.height):
    #     for x in range(patch.width):
    #         pixel = patch.get_pixel(x, y)  # get pixels from og image
    #         final_image.set_pixel(start_x + x, start_y + y, pixel)
    #     return final_image


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    # patch.show()  # test to see if image works. it does
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    # patch.show()  # image recolor test. good
    return patch


if __name__ == '__main__':
    main()
