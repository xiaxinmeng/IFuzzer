async def foo():
    lst = [await coro(i) for i in range(10)]
    return lst