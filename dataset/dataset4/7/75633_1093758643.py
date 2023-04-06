import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)

loop = asyncio.get_event_loop()

async def success_coro(seconds):
    await asyncio.sleep(seconds)
    print(seconds)


async def failed_coro(seconds):
    await asyncio.sleep(seconds)
    print(seconds)
    raise ZeroDivisionError

coros = [
    success_coro(2),
    failed_coro(3),
    success_coro(5),
]

async def waiter():
    await asyncio.gather(*coros)

asyncio.ensure_future(waiter())

loop.run_forever()