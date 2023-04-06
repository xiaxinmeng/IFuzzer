async def f():
    return (x for x in await g())

async def f():
    return (await x for x in g())