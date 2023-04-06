
async def foo():
    await asyncio.wait_for(bar())

t = asyncio.create_task(foo())
t.cancel()
