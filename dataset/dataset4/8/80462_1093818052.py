
import random
import concurrent.futures
import asyncio

executor = concurrent.futures.ProcessPoolExecutor()
ioloop = asyncio.get_event_loop()

async def func():
    result = await ioloop.run_in_executor(executor, random.random)
    executor.shutdown(wait=False)  # bug doesn't occur when `wait=True`

task = ioloop.create_task(func())
