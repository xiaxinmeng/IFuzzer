
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def wait_on_future():
    sleep(1)
    print(f.done()) # f is not done obviously
    f2 = executor.submit(pow, 5, 2)
    print(f2.result())
    sleep(1)    
    

executor = ThreadPoolExecutor(max_workers=100)
f = executor.submit(wait_on_future)
executor.shutdown(wait=True)
