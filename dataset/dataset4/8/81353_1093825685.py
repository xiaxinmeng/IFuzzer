async def test():
    await asyncio.gather(reader(), writer())