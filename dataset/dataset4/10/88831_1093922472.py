import asyncio
import gc

async def xyz():
    print("xyz")

event_loop = asyncio.get_event_loop()

event_loop.create_task(xyz())

t = event_loop.create_task(xyz())
del t

gc.collect()

event_loop.stop()
event_loop.run_forever()