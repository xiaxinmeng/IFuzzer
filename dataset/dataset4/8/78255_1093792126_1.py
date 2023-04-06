import asyncio

async def work():
    try:
        print('started working')
        await asyncio.sleep(3600)
    except BaseException as e:
        print('caught ' + str(type(e)))
    finally:
        print('finalization completed')

coro = work()
coro.send(None)
del coro