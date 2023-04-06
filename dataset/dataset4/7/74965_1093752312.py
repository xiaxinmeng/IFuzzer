import asyncio
import sys

limit = int(sys.argv[1])

async def double(x):
    await asyncio.sleep(1)
    return x * 2

async def print_doubles():
    coros = (double(x) for x in range(1000000))
    for res in asyncio.as_completed(coros, limit=limit):
        r = await res
        if r % 100000 == 0:
            print(r)

loop = asyncio.get_event_loop()
loop.run_until_complete(print_doubles())
loop.close()