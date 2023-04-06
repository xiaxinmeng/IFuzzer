
import asyncio
loop = asyncio.get_event_loop()

while True:
    loop.call_soon_threadsafe(loop.stop)
    loop.run_forever()
