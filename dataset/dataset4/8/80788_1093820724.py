
import asyncio
from threading import Thread


async def do_nothing():
    await asyncio.sleep(0)


async def loop_tasks():
    loop = asyncio.get_event_loop()
    while True:
        loop.create_task(do_nothing())
        await asyncio.sleep(0.01)


def old_thread():
    loop = asyncio.new_event_loop()
    while True:
        asyncio.tasks.Task.all_tasks(loop=loop)


def new_thread():
    loop = asyncio.new_event_loop()
    while True:
        asyncio.all_tasks(loop=loop)


old_t = Thread(target=old_thread)
new_t = Thread(target=new_thread)
old_t.start()
new_t.start()
asyncio.run(loop_tasks())
