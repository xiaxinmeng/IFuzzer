
async def foo():
    global inner
    inner = asyncio.create_task(foo())
    await asyncio.wait_for(inner)

asyncio.create_task(foo())
inner.cancel()
