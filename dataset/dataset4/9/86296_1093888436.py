

import asyncio


async def inner():
    return

async def with_for_coro():
    await asyncio.wait_for(inner(), timeout=100)
    await asyncio.sleep(1)
    print('End of with_for_coro. Should not be reached!')

async def main():
    task = asyncio.create_task(with_for_coro())
    await asyncio.sleep(0)
    assert not task.done()
    task.cancel()
    print('Called task.cancel()')
    await task  # -> You would expect a CancelledError to be raised.


asyncio.run(main())
