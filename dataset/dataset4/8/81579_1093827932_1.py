def foo():
    with sync_cm():
        return some_async_fn()