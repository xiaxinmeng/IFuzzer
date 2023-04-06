from multiprocessing import Pool
from time import sleep

def Process(x):
    try:
        print(x)
        sleep(.6-x/10.)
        raise Exception('Exception: %d' % x)
    finally:
        print('Finally: %d' % x)