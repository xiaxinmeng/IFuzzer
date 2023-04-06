test.py
import sys
sys.path.append("/Users/basnijholt/Downloads/cpython/Lib/concurrent/futures/")
from random import random
from process import ProcessPoolExecutor
import asyncio

ioloop = asyncio.get_event_loop()

async def func(ioloop, executor):
    result = await ioloop.run_in_executor(executor, random)
    executor.shutdown(wait=False)  # bug doesn't occur when `wait=True`

if __name__ == "__main__":
    executor = ProcessPoolExecutor()
    task = ioloop.run_until_complete(func(ioloop, executor))
