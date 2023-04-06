
import asyncio

async def agen():
    yield

async def main():
    p = agen()
    await asyncio.create_task(anext(p, 'finished'))

asyncio.run(main())
