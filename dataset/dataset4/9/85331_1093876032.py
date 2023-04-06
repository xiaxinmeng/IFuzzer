async def bar():
    return {
        n: await foo(n) for n in [1, 2, 3]
    }