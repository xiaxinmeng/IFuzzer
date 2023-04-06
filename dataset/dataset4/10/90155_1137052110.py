from asyncio import CancelledError
from asyncio import Semaphore
from asyncio import create_task
from asyncio import gather
from asyncio import run
from asyncio import sleep

async def process(idx, sem, tasks):
    await sleep(idx)
    async with sem:
        await sleep(2)
    tasks[1].cancel()

async def main():
    print('let me run for 3 seconds')
    sem = Semaphore(1)
    tasks = []
    for idx in range(2):
        tasks.append(create_task(process(idx, sem, tasks)))
    await sleep(3)
    await gather(*tasks, return_exceptions=True)

    print(f'sem._value == {sem._value}')
    print('sem is still...', end='', flush=True)
    async with sem:
        print('working!')

run(main())