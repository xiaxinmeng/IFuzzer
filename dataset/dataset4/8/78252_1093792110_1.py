task = asyncio.get_event_loop().create_task(ag())
print("type(task) is ", type(task))
print("asyncio.iscoroutine(task._coro)? ", asyncio.iscoroutine(task._coro))
print("repr(task) is ")
print(repr(task))