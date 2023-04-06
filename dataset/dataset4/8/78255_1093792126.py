import asyncio

async def work():
    try:
        print('started working')
        await asyncio.sleep(3600)
    except BaseException as e:
        print('caught ' + str(type(e)))
    finally:
        print('finalization completed')

async def stopper():
    await asyncio.sleep(5)
    loop.stop()

loop = asyncio.get_event_loop()
loop.create_task(work())
loop.create_task(stopper())
loop.run_forever()