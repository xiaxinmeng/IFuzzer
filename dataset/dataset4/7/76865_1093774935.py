import asyncio

async def test():
    while True:
        print('sleeping 1')
        await asyncio.gather(asyncio.sleep(1), return_exceptions=True)

async def amain():
    print('creating task')
    qwe = asyncio.Task(test())
    print('sleeping 2')
    await asyncio.sleep(2)
    print('cancelling task')
    qwe.cancel()
    print('waiting task for completion')
    try:
        await qwe
    except Exception as e:
        print('task complete: %r', e)

loop = asyncio.get_event_loop()
loop.run_until_complete(amain())