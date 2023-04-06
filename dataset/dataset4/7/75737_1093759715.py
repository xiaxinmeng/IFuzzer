import asyncio

@asyncio.coroutine
def foo():
    print(1)

loop = asyncio.get_event_loop()

fut = asyncio.wait_for(foo(), 0)

print('it is not raised yet')