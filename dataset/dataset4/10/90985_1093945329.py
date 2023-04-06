import asyncio
import random

async def job():
    await asyncio.sleep(5)

async def main():
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    r = random.random()
    if r < 0.5:
        task.cancel()
    else:
        task.cancel()
    await task

if __name__=="__main__":
    asyncio.run(main())