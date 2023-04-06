import asyncio
loop  = asyncio.get_event_loop()
async def coro(x):
    print(x)
    if x < 10:
        asyncio.create_task(coro(x+1))
    else:
        loop.stop()

loop.create_task(coro(0))
loop.stop()
loop.run_forever()