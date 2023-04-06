async def f():
    ...
yield from f()

@asyncio.coroutine
def g():
    ...
await g()