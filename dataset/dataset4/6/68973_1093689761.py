async def foo():
    await wrap_future(executor.submit(...))