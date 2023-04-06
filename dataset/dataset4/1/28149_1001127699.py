
import asyncio
from functools import partial


async def main():
    loop = asyncio.get_running_loop()

    async def work_coro(f_):
        await asyncio.wait_for(f_, timeout=5)
        while True:
            await asyncio.sleep(1)

    f = loop.create_future()
    loop.call_later(0.01, partial(f.set_result, object()))
    task = asyncio.create_task(work_coro(f))
    loop.call_later(0.01, partial(task.cancel))
    await asyncio.gather(task, return_exceptions=True)

asyncio.run(main())
