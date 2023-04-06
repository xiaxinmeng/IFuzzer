
import asyncio

async def job():
    # raise RuntimeError('error!')
    await asyncio.sleep(5)

async def main():
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    task.cancel('cancel job')
    await task

if __name__=="__main__":
    asyncio.run(main())
 