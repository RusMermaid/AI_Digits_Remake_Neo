from PIL import Image


def draw_digit(array_2d_digit):
    return [[Image.new("RGB",(1, 1),(int(10*j), int(10*j), int(10*j))) for j in i] for i in array_2d_digit]


