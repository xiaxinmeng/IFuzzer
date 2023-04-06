
import concurrent.futures
import time
import asyncio
import random

def get_progress(futures):
    return sum([f.done() for f in futures])

def long_task(t):
    time.sleep(1.5)
    return t

loop = asyncio.get_event_loop()
executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)
inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
futures_ = [loop.run_in_executor(executor, long_task, i) for i in inputs]

for i in range(5):
    time.sleep(1)
    print(get_progress(futures_))
