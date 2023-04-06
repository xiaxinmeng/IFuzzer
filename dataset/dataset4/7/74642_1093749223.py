async def get(process, key):
    try:
        return cache[key]
    except KeyError:
        if key in events:
            await events[key].wait()
        else:
            events[key] = asyncio.Event()