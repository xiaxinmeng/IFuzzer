async def arange(n):
    for i in range(n):
        yield i

async def alistcomp():
    return [i async for i in arange(10)]