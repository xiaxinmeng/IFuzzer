import asyncio

async def child():
    try:
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print("** Cancelled **")
        raise RuntimeError

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(child())
        await asyncio.sleep(0.5)
        raise asyncio.CancelledError

asyncio.run(main())