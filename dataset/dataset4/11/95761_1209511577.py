async def some_library(async_fn):
    try:
        await async_fn()
    except asyncio.CancelledError:
        raise
    except BaseException:
        # accidentally catching a BaseExceptionGroup('unhandled errors in a TaskGroup', [asyncio.CancelledError()])
        await cleanup()
        raise