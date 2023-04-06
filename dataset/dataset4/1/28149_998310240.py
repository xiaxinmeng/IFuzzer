
import asyncio


async def main():

    async def do_something():
        for _ in range(10):
            await asyncio.sleep(0.1)
        return object()

    async def work_coro():
        while True:
            await asyncio.wait_for(do_something(), timeout=5)

    task = asyncio.create_task(work_coro())
    await asyncio.sleep(1.0)  # needs adjustment to actually produce the race condition
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)

asyncio.run(main())

