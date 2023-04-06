#! /usr/bin/env python
import asyncio

async def func(i):
    print(i)
    if i >= 10:
        c = asyncio.current_task()
        c.print_stack()
        return
    await func(i+1)

loop = asyncio.get_event_loop()
loop.run_until_complete(func(1))
