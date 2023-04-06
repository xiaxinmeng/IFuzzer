from threading import current_thread
from concurrent.futures import ThreadPoolExecutor
from time import sleep

pool = ThreadPoolExecutor(100)

def f():
    print("I'm running in: ", current_thread().name)

def g():
    print("I'm running in: ", current_thread().name)
    for _ in range(100):
        pool.submit(f)
        sleep(0.1)

pool.submit(g)
sleep(1.5)