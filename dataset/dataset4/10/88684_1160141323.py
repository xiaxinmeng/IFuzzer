async def gen():
    try:
        yield 1
    finally:
        print('finalize inner')

async def func():
    try:
        async for x in gen():
            break
        await asyncio.sleep(0.1) # Switch task and run the finalizer 
    finally:
        print('finalize outer')

import asyncio
asyncio.run(func())
print('END')