import asyncio
import random

async def main():
    fut = asyncio.Future()
    fut.cancel()
    async def job():
        if random.random() < 0.5:
            await asyncio.sleep(2)
        fut.result()
        await asyncio.sleep(5)
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    task.cancel("cancel task")
    await task

asyncio.run(main())