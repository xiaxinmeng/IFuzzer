
#!/usr/bin/env python3

import os
import time
import psutil
import random
import concurrent.futures

from memory_profiler import profile as mem_profile

p = psutil.Process(os.getpid())

def do_magic(values):
    return None

@mem_profile
def foo():
    a = {i: chr(i) for i in range(1024)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        proccessed_data = pool.map(do_magic, a)

def fooer():
    while True:
        foo()
        time.sleep(1)

fooer()
