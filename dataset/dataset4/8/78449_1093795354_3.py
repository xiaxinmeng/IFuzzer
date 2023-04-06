
from concurrent.futures import ThreadPoolExecutor


def func(x, y):
    import time
    time.sleep(1)
    return x + y


def do_many():

    def callback(fut):
        global n
        result = fut.result()
        print('Got: ', result)
        n -= 1
        if n > 0:
            future = pool.submit(func, n, n)
            future.add_done_callback(callback)

    if n > 0:
        future = pool.submit(func, n, n)
        future.add_done_callback(callback)

n = 10
pool = ThreadPoolExecutor(max_workers=8)
do_many()
while n > 0:  # use while to block main thread
    pass
