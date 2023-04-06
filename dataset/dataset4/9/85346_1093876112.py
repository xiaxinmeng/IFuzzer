import asyncio
import inspect


@asyncio.coroutine
def foo():
    yield from asyncio.sleep(0)


print("isgeneratorfunction:", inspect.isgeneratorfunction(foo))