import asyncio

async def task():
    try:
        await asyncio.sleep(2)  # Will be interrupted after 1 second
    finally:
        1/0  # Crash in cleanup

async def main():
    async with asyncio.timeout(1):
        async with asyncio.TaskGroup() as tg:
            tg.create_task(task())
            await asyncio.sleep(1.5)

asyncio.run(main())