
task = asyncio.create_task(coroutine_function())
await asyncio.sleep(0)
assert not task.done()
task.cancel()
await task
