import asyncio

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(func())
finally:
    loop.close()