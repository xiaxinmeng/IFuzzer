import asyncio
async def main():
    coros = (asyncio.sleep(1), {1: 1})
    await asyncio.gather(*coros)
asyncio.run(main())