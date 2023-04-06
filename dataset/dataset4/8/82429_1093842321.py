import asyncio

# This gets cancelled normally
async def cancel_early():
    asyncio.current_task().cancel()
    await asyncio.sleep(1)

async def cancel_late():
    asyncio.current_task().cancel()
    # No sleep, so CancelledError doesn't get delivered until after the
    # task exits

async def main():
    t_early = asyncio.create_task(cancel_early())
    await asyncio.sleep(0.1)
    print(f"t_early.cancelled(): {t_early.cancelled()!r}")

    t_late = asyncio.create_task(cancel_late())
    await asyncio.sleep(0.1)
    print(f"t_late.cancelled(): {t_late.cancelled()!r}")
    print(f"t_late.exception(): {t_late.exception()!r}")

asyncio.run(main())