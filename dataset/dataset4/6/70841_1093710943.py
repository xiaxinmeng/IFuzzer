import asyncio
import functools

def foo(x): raise Exception()

loop = asyncio.get_event_loop()
loop.call_soon(functools.partial(foo, x=1))
loop.run_forever()