import asyncio
from contextlib import closing

with closing(asyncio.get_event_loop()) as loop:
    loop.run_until_complete(func())