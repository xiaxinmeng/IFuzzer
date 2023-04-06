@asyncio.coroutine
def outer_coro():
    @asyncio.coroutine
    def inner_coro():
        return 1

    return g()

result = loop.run_until_complete(outer_coro())