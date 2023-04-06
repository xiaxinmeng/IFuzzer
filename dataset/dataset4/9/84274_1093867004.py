
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def wait_on_future():
    sleep(1)
    f2 = executor.submit(pow, 5, 2)    
    print(f2.result())
    executor.shutdown(wait=True) #Uncomment/comment this makes no difference

executor = ThreadPoolExecutor(max_workers=100)
f = executor.submit(wait_on_future)
