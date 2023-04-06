
import sys, contextlib

@contextlib.contextmanager
def disable_coroutine_wrapping():
    wrapper = sys.get_coroutine_wrapper()
    sys.set_coroutine_wrapper(None)
    try:
        yield
    finally:
        sys.set_coroutine_wrapper(wrapper)

def wrapper(coro):
    async def wrap(coro):
        print("Coroutine started")
        result = await coro
        print("Coroutine finished")
        return result
    with disable_coroutine_wrapping():
        return wrap(coro)

sys.set_coroutine_wrapper(wrapper)

async def foo():
    print("Coroutine running")
    return "Coroutine result"

import asyncio
asyncio.get_event_loop().run_until_complete(foo())
