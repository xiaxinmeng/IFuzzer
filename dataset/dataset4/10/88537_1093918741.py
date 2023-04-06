import asyncio


async def inner():
    try:
        print(1)
        await asyncio.sleep(3600)
        print(2)
    except asyncio.CancelledError:
        print('inner - canc')
        raise


async def outer(f):
    try:
        print('a')
        # Version 1 - This creates the expected behaviour
        # await f
        # Version 2 - This creates the reversed behaviour
        await asyncio.wait_for(f, timeout=500)
        print('b')
    except asyncio.CancelledError:
        print('outer - canc')