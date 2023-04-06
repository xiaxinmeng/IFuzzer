
import asyncio

while True:
    loop = asyncio.new_event_loop()

    coro = loop.getaddrinfo('www.google.com', 80)

    task = asyncio.ensure_future(coro, loop=loop)

    task.cancel()

    loop.call_soon_threadsafe(loop.stop)

    loop.run_forever()

    loop.close()
