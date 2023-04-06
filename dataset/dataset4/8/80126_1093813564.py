import asyncio

async def task2func():
    await asyncio.sleep(2)

async def task1func(task2):
    try:
        await task2
    except asyncio.CancelledError:
        print("I don't know if I got cancelled")

async def main():
    loop = asyncio.get_event_loop()
    task2 = loop.create_task(task2func())
    task1 = loop.create_task(task1func(task2))
    await asyncio.sleep(0.5)

    print('Cancelling first task')
    task1.cancel()
    await task1