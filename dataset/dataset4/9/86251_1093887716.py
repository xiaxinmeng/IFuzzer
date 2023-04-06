
import asyncio
import time

N = 100000000

async def run():
    fut = asyncio.Future()
    fut.set_result(42)

    t0 = time.time()
    for _ in range(N):
        await fut
    t1 = time.time()
    print(f"Time: {t1 - t0} s")

asyncio.run(run())
