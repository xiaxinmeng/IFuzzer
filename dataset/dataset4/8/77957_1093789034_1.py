import asyncio
import time
import faulthandler

def bad():
    return {'nested': time.monotonic()}

faulthandler.enable()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

tasks = [asyncio.ensure_future(
    bad()
    for i in range(1)
)]
results_future = asyncio.gather(*tasks)

# Segmentation fault
results = loop.run_until_complete(results_future)