tasks = [asyncio.ensure_future(example(x)) for x in range(20)]
done, pending = await asyncio.wait(tasks, return_when=FIRST_EXCEPTION)
for fut in done:
    try:
        fut.result()
    except CancelException:
        for fut in pending:
            fut.cancel()