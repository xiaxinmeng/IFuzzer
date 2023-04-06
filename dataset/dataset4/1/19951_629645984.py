import asyncio, sys

async def nested():
    fut = asyncio.sleep(1)
    await fut  # AWAIT #1

async def run():
    task = asyncio.create_task(nested())
    await asyncio.sleep(0)
    task.cancel('POSSIBLY LONG CANCEL MESSAGE')

    await task  # AWAIT #2

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(run())
finally:
    loop.close()