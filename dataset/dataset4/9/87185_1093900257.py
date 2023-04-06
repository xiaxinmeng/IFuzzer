
import asyncio
import time

async def async_test():
    while True:
        await asyncio.sleep(1)
        print("in here - async")

def sync_test():
    while True:
        time.sleep(1)
        print("in here - sync")

async def main():
    async def tryexcept(func):
        try:
            await func
        except asyncio.exceptions.TimeoutError:
            print("error thrown")

    await tryexcept(asyncio.wait_for(async_test(), timeout=5))
    await tryexcept(asyncio.wait_for(asyncio.to_thread(sync_test), timeout=5))
    print("back in the main thread")

asyncio.run(main())
