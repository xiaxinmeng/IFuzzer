async def close_cancelling(agen):
    while True:
        try:
            task = asyncio.ensure_future(agen.__anext__())
            await task
            yield task.result()
        except (GeneratorExit, StopAsyncIteration):
            await agen.aclose()
            task.cancel()
            break


async def run():
    try:
        async for v in close_cancelling(agen):
            received.append(v)
    except asyncio.CancelledError:
        # handle finalization
        pass