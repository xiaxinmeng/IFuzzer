import asyncio
from time import time

async def my_func():
    return 1

async def gather_them():
    start_t = time()

    for _ in range(1000):
        coros = []
        for _ in range(3000):
            coros.append(await my_func())
        # await asyncio.gather(*coros)
        _ = [*coros]
    print(f"Cost {time() - start_t}s")

asyncio.run(gather_them())