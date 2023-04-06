@asyncio.coroutine
def idle():
    while 1:
        gc.collect()
        yield from asyncio.sleep(0.1)

asyncio.Task(idle())