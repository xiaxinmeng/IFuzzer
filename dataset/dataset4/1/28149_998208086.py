
import asyncio


async def main():
    evt = asyncio.Event()

    async def coroutine_function():
        try:
            resource = object()
            evt.set()  # to synchronize execution to an edge-case
            return resource
        finally:
            # simulate some time-consuming cleanup, during which:
            #   - this coroutine shall expect the result to be returned successfully
            #   - the coroutine is not done, so cancelling it is possible
            await asyncio.sleep(0.5)

    async def with_for_coro():
        await asyncio.wait_for(coroutine_function(), timeout=1)
        assert False, 'End of with_for_coro. Should not be reached!'

    task = asyncio.create_task(with_for_coro())
    await evt.wait()  # to synchronize execution to an edge-case
    assert not task.done()
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass
    else:
        assert False, "cancellation ignored"

asyncio.run(main())

