from multiprocessing import Process
import time

import gc
gc.set_debug(gc.DEBUG_STATS)

def foo():
    L = []
    L.append(L)

def worker():
    t = time.time() + .5
    while time.time() < t:
        foo()

p1 = Process(target=worker)
p2 = Process(target=worker)

p1.start()
p2.start()

p1.join()
p2.join()

p1.close()
p2.close()
