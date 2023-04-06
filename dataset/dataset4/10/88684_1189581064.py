import threading
import trio
import asyncio

async def gen(runner):
    try:
        yield 1
    finally:
        print(f'{runner=} finalize inner')

async def func(runner):
    try:
        async for x in gen(runner):
            break
    finally:
        print(f'{runner=} finalize outer')

print(f"{trio.run(func, 'trio')=}")
print(f"{asyncio.run(func('asyncio'))=}")
print(f"{func('manual').send(None)=}")  # on pypy3 this doesn't print finalize inner