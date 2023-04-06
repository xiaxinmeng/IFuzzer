import asyncio
from time import time

async def my_func():
    return 1

async def run_with_tg():
    start_t = time()
    for _ in range(1000):
        async with asyncio.TaskGroup() as tg:
            for _ in range(3000):
                tg.create_task(my_func())
    print(f"Cost {time() - start_t}s")

asyncio.run(run_with_tg())