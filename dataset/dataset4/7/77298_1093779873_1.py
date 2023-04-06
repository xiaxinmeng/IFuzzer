
# bpo33117.py. This needs to be called from a different thread as docs said but I am using future.result(timeout) just to make sure there is no error with respect to function argument.

import asyncio

loop = asyncio.get_event_loop()
timeout = 4

# Create a coroutine
coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3
