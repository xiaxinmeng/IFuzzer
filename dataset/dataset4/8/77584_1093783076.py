async def example(num):
    if x == 5:
        raise Exception('Exception that does not cancel')
    elif x == 15:
        raise CancelException()

tasks = [asyncio.ensure_future(example(x)) for x in range(20)]
done, pending = await asyncio.wait(tasks, return_when=FIRST_EXCEPTION, return_on=CancelException)