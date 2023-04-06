
#!/usr/bin/env python

import asyncio

async def task1():
    cv = asyncio.Condition()

    async with cv:
        await asyncio.wait_for(cv.wait(), 10)

async def main(loop):
    task = loop.create_task(task1())

    await asyncio.sleep(0)

    task.cancel()

    res = await asyncio.wait({task})

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main(loop))
