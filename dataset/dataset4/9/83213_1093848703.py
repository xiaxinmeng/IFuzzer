cond = asyncio.Condition()
async def coro():
    async with cond:
        await asyncio.wait_for(cond.wait(), timeout=999)