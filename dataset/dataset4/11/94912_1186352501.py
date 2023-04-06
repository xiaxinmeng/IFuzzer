async def _wrap_awaitable(awaitable): 
   """Helper for asyncio.ensure_future(). 
  
   Wraps awaitable (an object with __await__) into a coroutine 
   that will later be wrapped in a Task by ensure_future(). 
   """ 
   return await awaitable