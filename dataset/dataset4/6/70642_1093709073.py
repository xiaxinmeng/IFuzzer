import asyncio

async def bar():
    raise KeyboardInterrupt

loop = asyncio.get_event_loop()