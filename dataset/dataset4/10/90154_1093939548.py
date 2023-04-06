
import logging
import trio
from contextlib import asynccontextmanager

@asynccontextmanager
async def foo():
    await trio.sleep(1)
    yield


async def test():
    async with trio.open_nursery() as n:
        f = foo()
        n.start_soon(f.__aenter__)
        n.start_soon(f.__aenter__)

trio.run(test)

