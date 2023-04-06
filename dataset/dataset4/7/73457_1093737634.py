import asyncio

async def coro():
    print(asyncio.Task.all_tasks())
    print(asyncio.Task.all_tasks(None))

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())