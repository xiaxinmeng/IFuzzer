async def consumer(q: asyncio.Queue):
    while True:
        try:
            data = await q.get()
        except asyncio.CancelledError:
            q.put_nowait(None) # ignore QueueFull for this discussion
            continue