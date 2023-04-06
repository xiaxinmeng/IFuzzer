import asyncio
import traceback
from threading import Thread


class Test(Thread):
    def __init__(self):
        super().__init__()
        self.loop = asyncio.new_event_loop()

    async def getaddrinfo(self, loop):
        try:
            print(await loop.getaddrinfo("www.google.com", 8333))
        except Exception:
            print(traceback.format_exc())

    def run(self):
        loop = self.loop
        asyncio.set_event_loop(loop)
        asyncio.run_coroutine_threadsafe(self.getaddrinfo(loop), loop)
        loop.run_forever()


test = Test()
test.start()