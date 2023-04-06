
import asyncio
from threading import Thread


async def do_nothing(n=0):
    await asyncio.sleep(n)


async def loop_tasks():
    loop = asyncio.get_event_loop()
    while True:
        loop.create_task(do_nothing())
        await asyncio.sleep(0.01)


async def make_tasks(n):
    loop = asyncio.get_event_loop()
    for i in range(n):
        loop.create_task(do_nothing(1))
    await asyncio.sleep(1)


def make_lots_of_tasks():
    while True:
        asyncio.run(make_tasks(10000))


for i in range(10):
    t = Thread(target=make_lots_of_tasks)
    t.start()

asyncio.run(loop_tasks())
