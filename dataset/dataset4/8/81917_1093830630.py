import asyncio, contextlib

async def bad():
    while True:
        with contextlib.suppress(asyncio.CancelledError):
            await asyncio.sleep(1)
            print("running...")

if __name__ == '__main__':
    asyncio.run(asyncio.wait_for(bad(), 1))