async def wait():
    await f
    await f2
    await f3
ensure_future(wait())