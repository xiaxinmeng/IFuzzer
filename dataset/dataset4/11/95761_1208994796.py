import asyncio
import contextlib

class Sock:
    async def aclose():
        pass

async def foo():
    with contextlib.closing(Sock()):
        await asyncio.sleep(1)
        print("hello")


async def demo():
    task = asyncio.current_task()
    task.get_loop().call_later(0.1, task.cancel)
    try:
        await asyncio.gather(foo(), foo())
    except asyncio.CancelledError:
        pass # the intent here is to only reach it if asyncio.gather was cancelled cleanly


asyncio.run(demo())