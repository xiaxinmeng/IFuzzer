async def as_completed2(fs):
    pending = set(map(asyncio.ensure_future(fs)))
    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        yield from done