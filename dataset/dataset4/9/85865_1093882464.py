
import asyncio
import concurrent

def leaker_func():
    list(range(int(1000)))
    # removed 1/0 because this causes issues with the ProcessPoolExecutor

async def function():
    loop = asyncio.get_running_loop()
    for i in range(10000):
        loop.run_in_executor(concurrent.futures.ProcessPoolExecutor(), leaker_func)
