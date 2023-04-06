async def main():
    jobs = [uuid4().hex for i in range(1_000)]
    q = asyncio.Queue()
    for job in jobs:
        await q.put(job)

    t = asyncio.create_task(scheduler(q))
    await q.join()
    t.cancel()
    await t


if __name__ == "__main__":
    asyncio.run(main())