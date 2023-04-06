import asyncio

async def wait():
    await asyncio.sleep(5)

loop = asyncio.get_event_loop()
loop.run_until_complete(wait())