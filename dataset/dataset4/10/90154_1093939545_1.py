async def test():
    f = foo()
    await gather(f.__aenter__(), f.__aenter__())

run(test())