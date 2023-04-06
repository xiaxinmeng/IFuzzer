import concurrent.futures
import time

def bar(i):
    raise Exception(i) # Raise exception from the initializer

def foo(i):
    time.sleep(i)
    return "1"