def foo():
    async def inner():
        async for i in ai:
            yield i
    return inner