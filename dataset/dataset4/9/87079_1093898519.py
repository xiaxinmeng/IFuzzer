import asyncio
import gc

asyncio.set_event_loop(asyncio.ProactorEventLoop())
asyncio.set_event_loop(asyncio.ProactorEventLoop())
gc.collect()
asyncio.get_event_loop().run_forever()