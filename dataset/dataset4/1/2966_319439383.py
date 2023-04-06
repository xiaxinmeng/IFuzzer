import gc
import asyncio

class Evil:
    def __del__(self):
        gc.collect()


async def run():
    return Evil()


loop = asyncio.get_event_loop()

for i in range(100):
    loop.run_until_complete(asyncio.Task(run()))
#    f = asyncio.Future()
#    f.set_result(Evil())