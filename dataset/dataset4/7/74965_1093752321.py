async def igather(tasks, limit=None):
    pending = set()
    while True:
        for task in islice(tasks, limit - len(pending) if limit else None):
            pending.add(task)
        if pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                yield task
        else:
            break