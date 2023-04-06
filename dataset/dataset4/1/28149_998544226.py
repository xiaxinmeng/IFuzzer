
import asyncio


async def main():

    async def do_something():
        await asyncio.sleep(0.01)
        return object()

    async def work_coro():
        while True:
            await asyncio.wait_for(do_something(), timeout=5)

    for i in range(1000):
        print(i)
        task = asyncio.create_task(work_coro())
        await asyncio.sleep(0.01)
        task.cancel()
        await asyncio.gather(task, return_exceptions=True)

asyncio.run(main())

