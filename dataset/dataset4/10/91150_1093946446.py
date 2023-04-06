async def wrapper(coro):
    try:
        return await coro
    finally:
        context = contextvars.copy_context()
        # store the context copy somewhere