import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import sklearn.datasets
from PIL import Image

from Functions.F_draw_digit import draw_digit

digits = sklearn.datasets.load_digits()


print(digits.images[0])

digit = draw_digit(digits.images[0])
digit.save('digit-test.png')


