from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/karel.png')
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_sz pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_sz is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_sz pixels shaved off each
        side of the original image
    """
    new_width = (original_img.width - (trim_size * 2))  # 30 px off BOTH LEFT AND RIGHT
    new_height = (original_img.height - (trim_size * 2))  # 30 px off BOTH TOP AND BOTTOM

    cropped_img = SimpleImage.blank(new_width, new_height)

    for y in range(new_height):
        for x in range(new_width):
            orig_x =  x + trim_size
            orig_y =  y + trim_size
            pixel = original_img.get_pixel(orig_x, orig_y)
            cropped_img.set_pixel(x, y, pixel)

    return cropped_img
    
if __name__ == '__main__':
    main()
