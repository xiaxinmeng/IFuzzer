import os
import time
from multiprocessing import Pool

def initprocess():
    print("Starting PID: %d" % os.getpid())

def do_work(x):
    print("Doing work in %d" % os.getpid())
    time.sleep(x**2)

if __name__ == '__main__':
    p = Pool(2, initializer=initprocess,maxtasksperchild=1)
    results = p.map(do_work, (1,2), chunksize=1)