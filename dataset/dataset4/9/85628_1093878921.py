import asyncio

import time

import threading


def sync_test():
    time.sleep(1)

async def run_test():
    loop = asyncio.get_event_loop()

    for _ in range(10):
    #     r = await loop.getaddrinfo('wq.io', 443)
    #     print(r)

        loop.run_in_executor(None, sync_test)

    for t in threading.enumerate():
        print(t)


    while True:
        await asyncio.sleep(1)


asyncio.run(run_test())