import asyncio
import time

async def async_get_loop():
    start_time = time.time()
    for _ in range(5000000):
        asyncio.get_event_loop()
    return time.time() - start_time

loop = asyncio.get_event_loop()
results = []
for _ in range(10):
    start_time = time.time()
    result = loop.run_until_complete(async_get_loop())
    results.append(result)

import statistics
print("elapse time: %.3lf +- %.3lf secs" % (statistics.mean(results), statistics.stdev(results)))