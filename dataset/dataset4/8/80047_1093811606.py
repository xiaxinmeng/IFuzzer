import concurrent.futures
import sys

def f():
    import ctypes

while True:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        ftr = executor.submit(f)
        ftr.result()