import threading

async def gen():
    try:
        yield 1
    finally:
        print('finalize inner')

async def func():
    try:
        async for x in gen():
            break
    finally:
        print('finalize outer')

import threading

coro = func()
coro.send(None)