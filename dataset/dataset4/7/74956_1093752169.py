
import asyncio

loop = asyncio.get_event_loop()


async def consumer():
    while True:
        await asyncio.sleep(0)
        message = yield
        print('received', message)


async def amain():
    agenerator = consumer()
    await agenerator.asend(None)

    fa = asyncio.create_task(agenerator.asend('A'))
    fb = asyncio.create_task(agenerator.asend('B'))
    await fa
    await fb


loop.run_until_complete(amain())
