def __init__(self, loop=None):
    if loop is None:
        loop = asyncio._get_running_loop()
        if loop is None:
            # issue warning
            loop = asyncio.get_event_loop()