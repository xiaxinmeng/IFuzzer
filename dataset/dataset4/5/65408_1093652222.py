import asyncio
import os

def t1(q):
    yield from asyncio.sleep(0.5)
    q.put_nowait((0, 1, 2, 3, 4, 5))

def t2(q):
    v = yield from q.get()
    print(v)

q = asyncio.Queue()
asyncio.get_event_loop().run_until_complete(asyncio.wait([t1(q), t2(q)]))