import asyncio, traceback

async def raise_after(fut, delay):
    await asyncio.sleep(delay)
    fut.set_exception(TypeError(42))

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    loop.create_task(
        raise_after(fut, 1))

    print('hello ...')

    for i in range(3):
        try:
            print(await fut)
        except Exception as e:
            traceback.print_exception(e)

asyncio.run(main())
######################################################