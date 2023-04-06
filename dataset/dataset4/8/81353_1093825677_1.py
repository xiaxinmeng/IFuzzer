import asyncio

g1 = asyncio.Future()


async def writer():
    await asyncio.sleep(1)
    g1.set_result(41)

async def reader():
    await g1

async def test():
    await asyncio.gather(reader(), writer())

asyncio.run(test())