import asyncio


async def coro_with_error():
    # Coro raises en error with 1 sec delay
    await asyncio.sleep(1)
    raise Exception('Error in coro')


async def cancellator(coro):
    # We use this to cancel gather with delay 1 sec
    await asyncio.sleep(1)
    coro.cancel()


async def success_long_coro():
    # Long running coro, 2 sec
    try:
        await asyncio.sleep(2)
        print("I'm ok!")
        return 42
    except asyncio.CancelledError:
        # Track that this coro is really cancelled
        print('I was cancelled')
        raise


async def collector_with_error():
    gather = asyncio.gather(coro_with_error(), success_long_coro())
    try:
        await gather
    except Exception:
        print(f"WHOAGH ERROR, gather done={gather.done()}")
        print(f'EXC={type(gather.exception()).__name__}')
        # We want to cancel still running success_long_coro()
        gather.cancel()


async def collector_with_cancel():
    # Gather result from success_long_coro()
    gather = asyncio.gather(success_long_coro())
    # schedule cancel in 1 sec
    asyncio.create_task(cancellator(gather))
    try:
        await gather
    except Exception:
        print(f"WHOAGH ERROR, gather done={gather.done()}")
        print(f'EXC={type(gather.exception()).__name__}')
        # We want to cancel still running success_long_coro()
        gather.cancel()
        return

# First case, cancel gather when children are running
print('First case')
loop = asyncio.get_event_loop()
loop.create_task(collector_with_cancel())
# Ensure test coros we fully run
loop.run_until_complete(asyncio.sleep(3))
print('Done')

# Second case, cancel gather when child raise error
print('Second case')
loop = asyncio.get_event_loop()
loop.create_task(collector_with_error())
# Ensure test coros we fully run
loop.run_until_complete(asyncio.sleep(3))
print('Done')