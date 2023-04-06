import multiprocessing as mp
from multiprocessing.util import Finalize
import os
import time

def finalizer():
    time.sleep(0.2) # some time consuming work
    print('do cleanup work: {}'.format(os.getpid()))

def worker(_):
    print('do some work: {}'.format(os.getpid()))

def initializer():
    # ref: https://github.com/python/cpython/blob/master/Lib/multiprocessing/util.py#L147
    Finalize(None, finalizer, exitpriority=1)