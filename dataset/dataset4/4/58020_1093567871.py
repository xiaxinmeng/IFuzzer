
import multiprocessing as mp
import time


def g():
    time.sleep(100)

def f():
    mp.Process(target=g).start()
    1/0

mp.Process(target=f).start()
