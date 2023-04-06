
import asyncio
import sys

async def sleep_on_exc(inject):
    if inject:
        asyncio.ensure_future(inject_exc(coro))
    try:
        await asyncio.sleep(0.2)
        if not inject:
            print("Raising KeyboardInterrupt")
            raise KeyboardInterrupt()
    except KeyboardInterrupt:
        print("I'm not done yet")
        await asyncio.sleep(0.1)
        print("Now I'm done")

async def inject_exc(coro):
    await asyncio.sleep(0.1)
    print("Injecting KeyboardInterrupt")
    coro.throw(KeyboardInterrupt)

coro = sleep_on_exc(sys.argv[1] == "inject")
loop = asyncio.get_event_loop()
loop.run_until_complete(coro)
