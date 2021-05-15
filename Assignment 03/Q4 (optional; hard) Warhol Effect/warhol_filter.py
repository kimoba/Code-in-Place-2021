"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)

    # place a patch onto the final image
    # with its top left corner at ( start_x , start_y )
    put_patch(final_image, 0, 0, patch)  # column 1
    put_patch(final_image, 222, 0, patch)  # column 2
    put_patch(final_image, 444, 0, patch)  # column 3

    final_image.show()
    # patch.show()  # image recolor test. good


def put_patch(final_image, start_x, start_y, patch):
    '''
    final_image height: 444 (2 rows) Y
    final_image width: 666 (3 columns) X
    '''

    # # getting i values. max is patch_size dimension - 1 since we
    # # start at 0, 0
    # for y in range(patch.height):
    #     for x in range(patch.width):
    #         # for i in range(PATCH_SIZE):
    #             # print(i)
    #         pixel = patch.get_pixel(x, y)  # get pixels from og image
    #         final_image.set_pixel(x, y, pixel)

    # getting i values. max is patch_size dimension - 1 since we
    # start at 0, 0
    for y in range(patch.height):
        for x in range(patch.width):
            # for i in range(PATCH_SIZE):
                # print(i)
            pixel = patch.get_pixel(x, y)  # get pixels from og image
            final_image.set_pixel(start_x + x, start_y + y, pixel)


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
