import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import sklearn.datasets
from PIL import Image

from Functions.F_draw_digit import draw_digit

number_dataset = sklearn.datasets.load_digits()


print(number_dataset.images[0])


