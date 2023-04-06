def __init__(self, loop=None):
    if loop is None:
        loop = asyncio.get_event_loop()
        if not loop.is_running():
            # warn
            ...