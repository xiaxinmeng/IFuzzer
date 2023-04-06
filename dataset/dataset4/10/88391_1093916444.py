import asyncio
async def coro(x):
    print(x)
    if x < 10:
        asyncio.create_task(coro(x+1))
loop = asyncio.get_event_loop()
loop.create_task(coro(0))
loop.stop()
loop.run_forever()