import asyncio

l = asyncio.get_event_loop()
l.close()

async def foo():
    pass