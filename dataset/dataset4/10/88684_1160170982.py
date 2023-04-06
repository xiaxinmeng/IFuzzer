async def gen():
    try:
        yield 1
    finally:
        print('finalize inner')

async def func():
    try:
        async for x in gen():
            break
        # Schedules callback to create a task on next loop iteration 
    finally:
        await asyncio.sleep(0) # Creates a task to finalize gen
        await asyncio.sleep(0) # Run the task to finalize gen
        print('finalize outer')

import asyncio
asyncio.run(func())
print('END')