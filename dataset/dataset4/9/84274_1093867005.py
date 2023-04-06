
import concurrent.futures
import time

def test():    
    time.sleep(3)    
    print('test')

ex = concurrent.futures.ThreadPoolExecutor(max_workers=10)
ex.submit(test)
