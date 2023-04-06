import asyncio


async def tf(con):
    async with con:
        await asyncio.wait_for(con.wait(), 60)


async def f(loop):
    con = asyncio.Condition()

    t = loop.create_task(tf(con))

    await asyncio.sleep(1)
    t.cancel()

    async with con:
        con.notify_all()

    await t


loop = asyncio.get_event_loop()
loop.run_until_complete(f(loop))
