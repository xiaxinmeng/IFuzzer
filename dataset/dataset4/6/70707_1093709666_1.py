def is_awaitable(coro_or_future):
    if isinstance(coro_or_future, futures.Future):
        return coro_or_future
    elif asyncio.coroutines.iscoroutine(coro_or_future):
        return True
    elif asyncio.compat.PY35 and inspect.isawaitable(coro_or_future):
        return True
    else:
        return False