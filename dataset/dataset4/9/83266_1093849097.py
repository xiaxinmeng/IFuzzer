
import asyncio
import inspect

tracked_coro = None

async def main():
  # loop isn't entirely needed, just used to track event loop time
  loop = asyncio.get_running_loop()
  global tracked_coro
  tracked_coro = coro(loop)
  await asyncio.gather(tracked_coro, other_coro(loop))


# This is the coroutine being tracked
async def coro(loop):
  print(loop.time())
  print("Start of coro():",
           inspect.getcoroutinestate(tracked_coro))
  await nested_coro(loop)


async def nested_coro(loop):
  print(loop.time())
  # coro() is not suspended yet, because we did not reach a `yield`
  print("Start of nested_coro():",
           inspect.getcoroutinestate(tracked_coro))
  # This will call await `__sleep0()`, reaching a `yield` which suspends `coro()` and `nested_coro()`
  await asyncio.sleep(0)
  print(loop.time())
  print("After the await, coro() is resumed:",
           inspect.getcoroutinestate(tracked_coro))


async def other_coro(loop):
  print(loop.time())
  print("Start of other_coro():",
           inspect.getcoroutinestate(tracked_coro))

asyncio.run(main())
