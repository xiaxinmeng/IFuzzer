async def run_in_thread(func, /, *args, **kwargs):
  loop = asyncio.get_running_loop()
  func_call = functools.partial(func, *args, **kwargs)
  return await loop.run_in_executor(None, func_call)