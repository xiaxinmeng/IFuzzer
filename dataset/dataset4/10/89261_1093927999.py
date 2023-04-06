
while not task.cancel() and not task.cancelled():
    await asyncio.sleep(0)
