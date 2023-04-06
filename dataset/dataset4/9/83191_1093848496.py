
import asyncio
import threading

loop = asyncio.get_event_loop()

while True:
    def test():
        loop.call_soon_threadsafe(loop.stop)

    threading.Thread(target=test).start()
    loop.run_forever()

