import asyncio

async def task_timeout():
    condition = asyncio.Condition()
    with await condition:
        try:
            await asyncio.wait_for(condition.wait(), timeout=4)
        except asyncio.TimeoutError as e:
 
            print("timeout reached")
            # uncomment this line to make the code work
            # await asyncio.sleep(0)


f = asyncio.ensure_future(task_timeout())

loop= asyncio.get_event_loop()
loop.run_until_complete(f)