import asyncio

task_count = 10000

async def main():
    for x in range(1, task_count + 1):
        asyncio.ensure_future(f(x))

async def f(x):
    if x % 1000 == 0 or x == task_count:
        print(f'Run f({x})')
    await asyncio.sleep(1)
    loop.call_later(1, lambda: asyncio.ensure_future(f(x)))

loop = asyncio.get_event_loop()
loop.set_debug(True)
loop.run_until_complete(main())
loop.run_forever()