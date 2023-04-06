async def test():
    await asyncio.gather(reader(), reader(), writer())