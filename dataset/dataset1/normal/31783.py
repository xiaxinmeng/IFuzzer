from threading import current_thread
from concurrent.futures import ThreadPoolExecutor
from time import sleep

pool = ThreadPoolExecutor(4)

def f(_):
    print(current_thread().name)
    future = pool.submit(sleep, 0.1)
    future.add_done_callback(f)
    
f(None)
