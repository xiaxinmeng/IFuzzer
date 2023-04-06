
import concurrent.futures
import time

def test():    
    time.sleep(3)
    ex.submit(print, 'ex-print')
    print('test') #this is not printed

ex = concurrent.futures.ThreadPoolExecutor(max_workers=10)
ex.submit(test)
