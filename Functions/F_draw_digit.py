from PIL import Image  as IMG
from functools import reduce
def img_add_h(img1, img2=None):
	if img2 is None:
		return img1
	else:
		img_new = IMG.new("RGB", (img1.width + img2.width, max(img1.height, img2.height)))
		img_new.paste(img1, (0, 0))
		img_new.paste(img2, (img1.width, 0))
		return img_new

def img_add_v(img1, img2=None):
	if img2 is None:
		return img1
	else:
		img_new = IMG.new("RGB", (img1.width, img1.height + img2.height))
		img_new.paste(img1, (0, 0))
		img_new.paste(img2, (0, img1.height))
		return img_new

def img_add_list_2d(img_2d_list):  # Соединение изображений в 2d списке
    each_full_rows = [reduce(img_add_h, img_2d_list[i], img_2d_list[i].pop(0)) for i in range(len(img_2d_list))]
    full_img = reduce(img_add_v, each_full_rows)
    return full_img


def draw_digit(array_2d_digit):
    return img_add_list_2d([[IMG.new("RGB",(1, 1),(int(10*j), int(10*j), int(10*j))) for j in i] for i in array_2d_digit])


