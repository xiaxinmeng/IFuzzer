import sys
import multiprocessing

sys.stdout.close()

def foo():
    pass

p = multiprocessing.Process(target=foo)
p.start()