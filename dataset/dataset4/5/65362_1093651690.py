f = asyncio.Task(some_coroutine())
f.add_callback(some_completion_callback)
f = None