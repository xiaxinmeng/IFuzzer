async def test():
    return { n: [x async for x in elements(n)] for n in range(3)}