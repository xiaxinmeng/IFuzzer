from time import time
from asyncio import run, create_task, sleep

async def task(name, n): 
    for i in range(n):
        print(f"task-{name}: ", i, time())
        await sleep(1)

async def top():
    t0 = create_task(task("T0", 10))
    t1 = create_task(task("T1", 10))
    print("starting tasks ...")
    await t0
    await t1

run(top())