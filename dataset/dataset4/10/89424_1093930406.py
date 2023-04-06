import skimage
import numpy as np
import timeit

nrep = 16

def run_complement(img):
    def inner():
        skimage.util.invert(img)
    return inner

img = np.random.randint(0, 65535, (512, 512, 3), dtype='uint16')