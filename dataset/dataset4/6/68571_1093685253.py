from asyncio import wrap_future

async def foo():
    await wrap_future(executor.submit(...))