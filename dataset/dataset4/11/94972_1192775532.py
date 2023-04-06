import weakref
import asyncio
import gc

import objgraph
import logging


logger = logging.getLogger(__name__)


async def async_fn():
    try:
        await asyncio.get_running_loop().create_future()
    except BaseException:
        logger.exception("closed!")
        raise


async def amain():
    weak_task = weakref.ref(asyncio.create_task(async_fn()))
    await asyncio.sleep(0.01)
    gc.collect()
    print(weak_task())


async def sheild_gc():
    strong_shielded_fut = asyncio.shield(async_fn())
    await asyncio.sleep(0)
    asyncio.current_task().cancel()
    try:
        await strong_shielded_fut
    except asyncio.CancelledError:
        pass

    gc.collect()


asyncio.run(amain())
print("======================")
asyncio.run(sheild_gc())