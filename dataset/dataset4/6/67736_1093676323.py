import asyncio
import atexit

def close_asyncio_loop():
    loop = None
    try:
        loop = asyncio.get_event_loop()
    except AttributeError:
        pass
    if loop is not None:
        loop.close()

atexit.register(close_asyncio_loop)