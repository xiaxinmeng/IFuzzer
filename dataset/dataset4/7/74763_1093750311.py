
import asyncio, sys

def wrapper(coro):
    @asyncio.coroutine
    def wrap(coro):
        print("Coroutine started")
        result = yield from coro
        print("Coroutine finished")
        return result
    return wrap(coro)

sys.set_coroutine_wrapper(wrapper)

async def foo():
    print("Coroutine running")
    return "Coroutine result"

import asyncio
asyncio.get_event_loop().run_until_complete(foo())
