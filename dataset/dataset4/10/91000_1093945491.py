tg = asyncio.TaskGroup()
...
async with tg:
  with asyncio.TaskGroupBinder(tg):  # just a hypothetical API
    asyncio.create_task(...)         # equivalent to tg.create_task(...)
    await some_library.some_work()   # all tasks are bound to tg
  asyncio.create_task(...)           # fire-and-forget (not bound to tg)