import asyncio
import threading


fut = asyncio.Future()

async def coro(loop):
    fut.add_done_callback(lambda _: loop.stop())
    loop.call_later(1, fut.set_result, None)
    while True:
        await asyncio.sleep(100000)

def run():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro(loop))
    loop.close()


t = threading.Thread(target=run)
t.start()
t.join()