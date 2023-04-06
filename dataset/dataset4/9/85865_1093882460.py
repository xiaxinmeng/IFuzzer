
import asyncio

def leaker():
    x = list(range(int(1000)))
    1/0

async def function():
    loop = asyncio.get_running_loop()
    for i in range(10000):
        loop.run_in_executor(None, leaker)
