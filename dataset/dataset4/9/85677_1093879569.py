from uuid import uuid4
import asyncio, random


async def worker(q: asyncio.Queue):
    while job := await q.get():
        print(f"working on job {job}")
        await asyncio.sleep(random.random() * 5)
        print(f"Completed job {job}")
        q.task_done()


async def scheduler(q, max_concurrency=5):
    workers = []
    for i in range(max_concurrency):
        w = asyncio.create_task(worker(q))
        workers.append(w)