import asyncio
fut = asyncio.Future()
try:
    raise ValueError()
except Exception as err:
    fut.set_exception(err)
