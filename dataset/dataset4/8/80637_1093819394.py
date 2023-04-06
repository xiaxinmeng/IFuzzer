
import asyncio


async def test():
    async def f():
        await g_task

    async def g():
        await f_task

    f_task = asyncio.create_task(f())
    g_task = asyncio.create_task(g())

    async def release():
        await asyncio.sleep(5)
        f_task.cancel()

    await asyncio.gather(f_task, g_task, release())

asyncio.run(test())
