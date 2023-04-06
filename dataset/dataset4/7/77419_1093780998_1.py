import asyncio
import concurrent.futures

f = concurrent.futures.Future()
async_f = asyncio.wrap_future(f)
f.set_result(1)
f.set_result(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(async_f)