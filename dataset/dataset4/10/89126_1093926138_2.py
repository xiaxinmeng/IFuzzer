
import asyncio
import contextlib

async def agen():
    await asyncio.sleep(1)
    yield

async def main():
    async with contextlib.aclosing(agen()) as p:
        asyncio.current_task().cancel()
        try:
            await anext(p, 'finished')
        except asyncio.CancelledError:
            pass

asyncio.run(main())
