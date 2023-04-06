async def bar():
    return {
        i: {
            n: await foo(n) for n in [1, 2, 3]
        } for i in [1,2,3]
    }