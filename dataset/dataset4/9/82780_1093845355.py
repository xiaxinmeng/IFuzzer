import asyncio

q = asyncio.Queue()

async def main():
    await asyncio.gather(q.put(1), q.get(1))

asyncio.run(main())