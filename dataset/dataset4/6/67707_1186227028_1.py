import inspect
import functools
import asyncio

async def demo(v):
    pass


@asyncio.coroutine
def demo_old(v):
    pass


print(f"{inspect.iscoroutinefunction(functools.partial(demo, v=1))=}")
print(f"{asyncio.iscoroutinefunction(functools.partial(demo, v=1))=}")
print(f"{inspect.iscoroutinefunction(functools.partial(demo_old, v=1))=}")
print(f"{asyncio.iscoroutinefunction(functools.partial(demo_old, v=1))=}")

# this prints:
# /home/graingert/projects/bar.py:10: DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
#   def demo_old(v):
# inspect.iscoroutinefunction(functools.partial(demo, v=1))=True
# asyncio.iscoroutinefunction(functools.partial(demo, v=1))=True
# inspect.iscoroutinefunction(functools.partial(demo_old, v=1))=False
# asyncio.iscoroutinefunction(functools.partial(demo_old, v=1))=False