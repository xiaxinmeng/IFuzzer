import asyncio


async def writer():
    await asyncio.sleep(1)
    g1.set_result(41)

async def reader():
    await g1

async def test():
    global g1
    g1 = asyncio.Future()
    await asyncio.gather(reader(), writer())

asyncio.run(test())