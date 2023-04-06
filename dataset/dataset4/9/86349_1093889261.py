
import asyncio

async def func():
    return asyncio.all_tasks()

async def main():
    print(await asyncio.wait_for(func(), timeout=10))

asyncio.run(main())
