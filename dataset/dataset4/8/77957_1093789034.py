import asyncio
import time
import faulthandler

faulthandler.enable()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Note that ensure_future argument is generator
# which yields time.monotonic() return value
tasks = [asyncio.ensure_future(
    time.monotonic()
    for i in range(1)
)]
results_future = asyncio.gather(*tasks)

# Segmentation fault
results = loop.run_until_complete(results_future)